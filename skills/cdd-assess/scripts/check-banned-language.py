#!/usr/bin/env python3
"""Detect decision/action language that should not appear in CDD assessment reports."""
from __future__ import annotations
import re
import sys
from pathlib import Path

TERMS = [
    "approve", "approved", "approval", "reject", "rejected", "decline", "declined",
    "escalate", "escalation", "must obtain", "should request", "recommend", "recommended",
    "recommendation", "condition precedent", "next steps", "remediate", "acceptable",
    "unacceptable",
]
PATTERN = re.compile(r"\b(" + "|".join(re.escape(t) for t in TERMS) + r")\b", re.I)

# Mandatory report boilerplate that legitimately contains banned terms. These
# exact snippets are removed from a line before matching; everything else on
# the line is still checked.
ALLOWED_SNIPPETS = [
    "Not a regulatory determination, approval, recommendation, or instruction",
    "no approval, decline, escalation, condition, next-action, or recommendation language",
]


def check_line(line: str) -> re.Match | None:
    for snippet in ALLOWED_SNIPPETS:
        line = line.replace(snippet, "")
    return PATTERN.search(line)


def self_test() -> int:
    cases = [
        # (line, should_flag)
        ("Drafted by an AI assistant for review by a qualified compliance professional. "
         "Not a regulatory determination, approval, recommendation, or instruction.", False),
        ("This report contains no approval, decline, escalation, condition, next-action, "
         "or recommendation language.", False),
        ("We recommend approval of this client.", True),
        ("The reviewer should request updated statements.", True),
        ("The declared amounts reconcile with bank statements.", False),
        ("Not a regulatory determination, approval, recommendation, or instruction. "
         "Escalate to the MLRO.", True),
    ]
    failures = 0
    for line, should_flag in cases:
        flagged = check_line(line) is not None
        if flagged != should_flag:
            failures += 1
            print(f"self-test FAIL (expected flag={should_flag}): {line}")
    if failures:
        return 1
    print(f"self-test OK: {len(cases)} cases")
    return 0


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) < 2:
        print("Usage: check-banned-language.py [--self-test] <file> [<file> ...]", file=sys.stderr)
        return 2
    found = False
    for arg in sys.argv[1:]:
        path = Path(arg)
        text = path.read_text(errors="ignore")
        for i, line in enumerate(text.splitlines(), 1):
            if check_line(line):
                found = True
                print(f"{path}:{i}: {line.strip()}")
    return 1 if found else 0

if __name__ == "__main__":
    raise SystemExit(main())
