#!/usr/bin/env python3
"""Flag weak citation patterns in draft CDD reports or bundle files."""
from __future__ import annotations
import re
import sys
from pathlib import Path

BARE_SOURCE = re.compile(r"\[(S\d+)\]")
SOURCE_RANGE = re.compile(r"\[S\d+\s*[-–]\s*S\d+\]")
BAD_SOURCE_WORDS = re.compile(r"\b(script|pipeline|review-bundle|analysis\.md|record\.md)\b", re.I)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate-citations.py <file> [<file> ...]", file=sys.stderr)
        return 2
    found = False
    for arg in sys.argv[1:]:
        path = Path(arg)
        text = path.read_text(errors="ignore")
        for i, line in enumerate(text.splitlines(), 1):
            problems = []
            if BARE_SOURCE.search(line):
                problems.append("bare source citation")
            if SOURCE_RANGE.search(line):
                problems.append("source range citation")
            if "Source:" in line and BAD_SOURCE_WORDS.search(line):
                problems.append("source line appears to cite tooling/bundle")
            if problems:
                found = True
                print(f"{path}:{i}: {', '.join(problems)}: {line.strip()}")
    return 1 if found else 0

if __name__ == "__main__":
    raise SystemExit(main())
