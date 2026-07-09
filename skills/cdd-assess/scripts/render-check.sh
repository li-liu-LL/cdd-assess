#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: render-check.sh <report.html>" >&2
  exit 2
fi

REPORT="$1"
if [[ ! -f "$REPORT" ]]; then
  echo "Report not found: $REPORT" >&2
  exit 2
fi

SCRATCH="${TMPDIR:-/tmp}/cdd-render-check-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$SCRATCH"
BASE="$(basename "$REPORT" .html)"
ABS="$(cd "$(dirname "$REPORT")" && pwd)/$(basename "$REPORT")"

if ! command -v google-chrome >/dev/null 2>&1; then
  echo "google-chrome not found; render check cannot run automatically." >&2
  echo "Open manually with file://$ABS and print to PDF for inspection." >&2
  exit 1
fi

google-chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$SCRATCH/$BASE.pdf" "file://$ABS"

google-chrome --headless --no-sandbox --disable-gpu --window-size=1280,2000 \
  --screenshot="$SCRATCH/$BASE.png" "file://$ABS"

echo "Render artifacts:"
echo "PDF: $SCRATCH/$BASE.pdf"
echo "Screenshot: $SCRATCH/$BASE.png"
echo "Inspect for page numbers, table fit, watermark overlap, figure readability, blank pages, and broken cards/captions."
