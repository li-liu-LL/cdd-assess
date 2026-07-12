#!/usr/bin/env python3
"""Validate the required review-bundle structure for one or more bundle directories."""
from __future__ import annotations
import sys
from pathlib import Path

REQUIRED = {
    "record.md": ["# Factual Record", "## Source Register", "## CDD Form Completeness",
                  "## Completeness Checklist"],
    "analysis.md": ["# Analysis", "## Licensing Assessment", "## Consistency Sweep",
                    "## Risk Assessment", "## EDD Triggers", "## Arithmetic check"],
    "composition.md": ["# Composition Plan", "## Executive Summary Plan",
                       "## Observation Cards", "## Figure And Exhibit Plan",
                       "## Recommendation Rationale Plan"],
    "conflicts-and-gaps.md": ["# Conflicts And Gaps", "## Outstanding Information Register",
                              "## Outstanding Documents Register", "## Clarification Register"],
}


def check_bundle(root: Path) -> bool:
    failed = False
    for name, headings in REQUIRED.items():
        path = root / name
        if not path.exists():
            print(f"missing: {path}")
            failed = True
            continue
        text = path.read_text(errors="ignore")
        for heading in headings:
            if heading not in text:
                print(f"missing heading in {path}: {heading}")
                failed = True
    return failed


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate-bundle.py <review-bundle-dir> [<review-bundle-dir> ...]",
              file=sys.stderr)
        return 2
    failed = False
    for arg in sys.argv[1:]:
        root = Path(arg)
        if not root.is_dir():
            print(f"not a directory: {root}")
            failed = True
            continue
        if check_bundle(root):
            failed = True
        else:
            print(f"ok: {root}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
