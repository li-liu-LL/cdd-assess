#!/usr/bin/env python3
"""Check that decision/action language appears only inside decision zones.

Decision language (ratings, recommendations, conditions, EDD determinations)
belongs in the executive summary and Part I only. Those regions are wrapped in
markers in the report HTML:

    <!-- decision-zone: start -->
    ...
    <!-- decision-zone: end -->

Anything matching the decision-term list outside a zone is flagged, except the
mandatory boilerplate snippets below.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

TERMS = [
    "approve", "approved", "approval", "reject", "rejected", "decline", "declined",
    "escalate", "escalation", "must obtain", "should request", "recommend", "recommended",
    "recommendation", "condition precedent", "conditions precedent", "next steps",
    "remediate", "acceptable", "unacceptable", "edd required", "onboard", "onboarded",
]
PATTERN = re.compile(r"\b(" + "|".join(re.escape(t) for t in TERMS) + r")\b", re.I)

ZONE_START = re.compile(r"<!--\s*decision-zone:\s*start\s*-->", re.I)
ZONE_END = re.compile(r"<!--\s*decision-zone:\s*end\s*-->", re.I)

# Mandatory boilerplate and section titles that legitimately carry decision
# terms outside a zone (cover/final-page disclaimer, table of contents).
ALLOWED_SNIPPETS = [
    "The risk rating and recommendation are draft proposals requiring review and "
    "approval by a qualified compliance officer before any onboarding action",
    "Risk Assessment and Recommendation",
    "Final Compliance Recommendation",
    "Acceptable Alternative",
    'href="#recommendation"',
    "onboarding assessment",
    "onboarding materials",
]


def check_line(line: str) -> re.Match | None:
    for snippet in ALLOWED_SNIPPETS:
        line = line.replace(snippet, "")
    return PATTERN.search(line)


def check_file(path: Path) -> bool:
    """Return True if problems were found."""
    found = False
    in_zone = False
    text = path.read_text(errors="ignore")
    for i, line in enumerate(text.splitlines(), 1):
        if ZONE_START.search(line):
            if in_zone:
                print(f"{path}:{i}: nested decision-zone start")
                found = True
            in_zone = True
            continue
        if ZONE_END.search(line):
            if not in_zone:
                print(f"{path}:{i}: decision-zone end without start")
                found = True
            in_zone = False
            continue
        if not in_zone and check_line(line):
            found = True
            print(f"{path}:{i}: decision language outside decision zone: {line.strip()}")
    if in_zone:
        print(f"{path}: decision-zone start without end")
        found = True
    return found


def self_test() -> int:
    doc = "\n".join([
        "Drafted by an AI assistant. The risk rating and recommendation are draft "
        "proposals requiring review and approval by a qualified compliance officer "
        "before any onboarding action. Not a regulatory determination.",
        "Part I – Risk Assessment and Recommendation",
        '<li><a href="#recommendation">Final Compliance Recommendation</a></li>',
        "<th>Acceptable Alternative</th>",
        "The bank statement records a rental credit of SGD 4,200.",
        "<!-- decision-zone: start -->",
        "Recommendation: Conditional Approval. EDD Required: No.",
        "Conditions precedent: submission of outstanding documents (ref D1).",
        "<!-- decision-zone: end -->",
        "The declared amounts reconcile with the register extract.",
    ])
    bad_doc = doc + "\nWe recommend approval of this customer."
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(doc)
        good = Path(f.name)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(bad_doc)
        bad = Path(f.name)
    failures = 0
    if check_file(good):
        print("self-test FAIL: compliant document was flagged")
        failures += 1
    if not check_file(bad):
        print("self-test FAIL: leaked decision language was not flagged")
        failures += 1
    good.unlink()
    bad.unlink()
    if failures:
        return 1
    print("self-test OK")
    return 0


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) < 2:
        print("Usage: check-decision-language.py [--self-test] <file> [<file> ...]",
              file=sys.stderr)
        return 2
    found = False
    for arg in sys.argv[1:]:
        if check_file(Path(arg)):
            found = True
    return 1 if found else 0

if __name__ == "__main__":
    raise SystemExit(main())
