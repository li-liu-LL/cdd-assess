# Report Rendering

Use `assets/report-template.html` and `assets/report.css` as the default internal report presentation. Copy them into the case workspace `assets/` folder before editing so the skill remains reusable. The template is adaptable: change section order, labels, exhibits, page breaks, and layout in response to user feedback or case-specific evidence, while preserving mandatory coverage, citations, page numbering, and render checks. The rendered HTML must also resolve its linked assets from its own location: either copy `report.css`, logo, and watermark beside each versioned HTML file in `client-packs/*/reports/`, or adjust the links to the workspace `assets/` folder. Verify the report with `file://` rendering, not only in an editor preview.

## Versioning

- First report: `reports/v001-{customer-type}-{short-customer-name}-onboarding-assessment.html`.
- Examples: `v001-individual-jane-tan-onboarding-assessment.html`, `v001-corporate-acme-pte-ltd-onboarding-assessment.html`.
- Each material factual change, reviewer-comment round, or research refresh creates the next version.
- Record version, date, preparer, basis of change, source bundle, and reviewer comments in the report.

## Document Apparatus

Every report carries, in addition to its sections:

- **Compact dossier header**: logo, classification, title, and a metadata grid that fits above the fold on screen and within the first half page in print. The header never consumes a full printed page. If the operating context was incomplete and drafting proceeded on officer-directed working assumptions, the header carries a context-status line naming the assumed frame.
- **Table of contents**: section numbers and titles, immediately after the header.
- **Key-figures band** at the top of the reviewer brief: four to six quantified figures a reviewer needs first — declared net worth or net assets, independently corroborated amount and coverage, source counts split independent versus customer representation, conflicts found, and human-verification items.
- **Exhibit register**: a table in the Evidence Exhibits section listing every exhibit with number, title, sources, and artifact type. Exhibits are numbered `Exhibit 1..n` and cited by number from the body.
- **Appendix**: fact tables longer than roughly eight rows move to an appendix, leaving a summarized table plus narrative in the body.

## Figures

- Every report includes a financial corroboration figure: declared components versus independently evidenced amounts, drawn as an inline SVG bar composition with values labelled in text.
- Corporate reports include an ownership-and-control diagram as inline SVG: one node per natural person and entity, ownership percentages on edges, control roles (director, signatory) marked on nodes. Do not draw structure diagrams as ASCII in `pre` blocks.
- Every figure carries the academic caption apparatus, in this order: numbered kicker (`Figure n`, automatic via CSS), a short bold headline stating the figure's finding, a subtitle giving units and scope, the artifact itself, then a `figcaption` with a **Notes:** line (how to read it, assumptions, limits) and a **Source:** line (field-level citations, extraction method, confidence). Body text cites figures by number.
- Follow the data-ink discipline: no enclosing boxes, backgrounds, or decorative borders around charts; hairline rules only; light or no gridlines; values labelled directly on marks instead of axes where the data is sparse; every drop of non-data ink must earn its place.
- Figures encode values as visible text inside the SVG so the figure survives grayscale print and screen readers; color differences are reinforced by labels or patterns.
- **A bar is a magnitude.** Never draw a bar, wedge, or area for `not observed`, `not applicable`, or a placeholder value. When a declared amount is absent, the corroboration figure degrades to the evidenced-baseline bars only, with a text line stating that no declared amount was observed — or the figure is replaced by a stat line. A full-width bar labelled "not observed" misreads as a huge value.
- **Diagram layout rules** (ownership maps, flow diagrams): labels never sit on top of edges or other labels — offset them and connect with a short leader line; minimum one text-line height of clear space between nodes; edge labels shorter than the gap they annotate, else move the detail into the node; the customer/root node carries its name, never a generic placeholder; test at three or more nodes per tier before accepting the layout. If a structure is too deep to draw legibly, draw the top layers and put the full chain in the ownership table.
- **Source lines cite evidence, never tooling.** Figure and exhibit `Source:` lines reference client materials and persisted research findings at field level. Scripts, review-bundle paths, and pipeline files are not sources and never appear in a report.
- Screenshots and crops sit near the facts they support and cite source, page, and extraction method. If a critical exhibit has no visual artifact, record `No visual evidence generated` with the reason.

## Presentation Rules

- The layout language is a restrained editorial style: serif narrative text with a sans-serif data layer (tables, labels, captions), a short red tab rule as the masthead and figure accent, unboxed figures and cards, hairline table rules, and generous whitespace. Decoration that carries no information is removed rather than styled.
- Treat presentation as evidence design. The first screen and first printed page should let the reviewer identify the client, report version, confidentiality, and the first four to six material figures without hunting.
- Apply typography rules at the document level: root font smoothing, balanced wrapping for headings and figure titles, pretty wrapping for short paragraphs/captions/list items, and stable line lengths for narrative text. Do not scale font size from viewport width; printed reports need deterministic typography.
- Use tabular numerals for key figures, numeric table columns, percentages, ownership percentages, money amounts, source counts, and figure labels. Align comparable numeric columns on the right except for identifiers such as passport numbers or registration numbers.
- Use surface treatment sparingly. The report sheet may have a subtle transparent screen shadow; sections, figures, and observation cards stay unboxed unless a border or rule carries information. Never place a card inside another card.
- Keep border radii conservative when a local brand style adds rounded surfaces. If a rounded element is nested inside another, set the outer radius equal to inner radius plus the visual padding. Prefer square or lightly rounded report surfaces over app-like pills.
- Give screenshots, document crops, and photo evidence a 1px inset neutral outline so their edges remain legible on white paper. Use `rgba(0, 0, 0, 0.1)` in light reports and `rgba(255, 255, 255, 0.1)` in dark variants; do not tint evidence outlines with the brand palette.
- Avoid decorative animation, hover-only affordances, or interaction-dependent disclosure in deliverable reports. If a screen-only preview adds a transition, specify the exact properties and keep it out of print. Do not use `transition: all`.
- Mark the report `Internal Compliance Use Only`.
- Show customer type and short customer name in the report title and version metadata.
- Include logo and watermark slots even when placeholders are used.
- Lead major analytical sections with sourced prose per `references/report-composition.md`. Use tables for factual records, source inventories, document gaps, SOW/SOF calculations, net worth corroboration, and UBO mapping.
- Cite facts inline with the field-level source labels defined in `references/report-composition.md`.
- Keep assessment observations separate from facts; render them as observation cards.
- Wrap the executive summary and Part I in decision-zone markers (`<!-- decision-zone: start -->` / `<!-- decision-zone: end -->`); decision language appears nowhere outside them, verified by `scripts/check-decision-language.py`.

## Print And Accessibility Rules

- Use semantic HTML: `main`, `header`, `section`, `nav` for the TOC, ordered headings, `figure`, `figcaption`, and table headers.
- Keep material content as text; screenshots support nearby extracted text but do not replace it.
- Do not rely on color alone for confidence, risk, or gap status.
- Print as A4 portrait with page numbers. Preserve the CSS `@page` counter rules unless the user supplies a different print standard, and inspect the PDF to confirm page numbers appear.
- Use explicit print-only page breaks before major transitions such as exhibits, observations, or appendices when they improve scanability. Avoid creating mostly blank pages.
- Set table cells to wrap long citations, filenames, wallet addresses, identifiers, and source paths without forcing horizontal overflow. In screen views, horizontal scrolling is acceptable only for small screens; in print, wide tables move to an appendix or smaller table type.
- Scope small-screen adaptations to `@media screen and (max-width: …)` so they can never fire in print. Print layout is controlled only by `@media print`.
- Body tables must fit the printable A4 width: prefer six columns or fewer; give wider tables a smaller print font or move them to the appendix. Never rely on horizontal scrolling in print.
- Avoid page breaks inside short notes, observation cards, figures, captions, and compact tables. Allow long tables to break naturally with `thead` repeating.
- In print, reduce decorative color, shadows, and watermark opacity; preserve citations and source labels.
- The disclaimer appears on the cover and final page.

## Render Check

Render every report to PDF and screenshot before delivery and look at the output. Render-check artifacts are disposable: write them to a scratch or temporary directory outside the case workspace and discard them after inspection — the versioned HTML in `reports/` is the deliverable.

```bash
google-chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$SCRATCH/{report}.pdf" "file://$PWD/{report}.html"
google-chrome --headless --no-sandbox --disable-gpu --window-size=1280,2000 \
  --screenshot="$SCRATCH/{report}.png" "file://$PWD/{report}.html"
```

Use `--no-pdf-header-footer` (or the equivalent print dialog setting) so the browser's file-path header/footer does not appear on internal reports.

Inspect the PDF for: missing page numbers, truncated table columns, rendered scrollbars, a header or metadata block consuming a full page, text overlapping the watermark, unreadable figure text, clipped or orphaned one-word heading wraps, mostly blank forced-break pages, and page breaks inside cards or captions. Confirm the exhibit register row count equals the number of figures rendered (this count belongs in the arithmetic check). Any failure fails the render check.

Content-quality criteria live in the phase completion gates in `SKILL.md` and `references/final-self-check.md` — this file governs presentation and print behavior only.
