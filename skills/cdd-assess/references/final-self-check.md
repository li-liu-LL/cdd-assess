# Final Self-Check

Run this checklist before delivery. If any item fails, revise the bundle/report or mark the unresolved issue for human verification.

## Workspace And Grounding

- Original source drop is preserved.
- `OPERATING_CONTEXT.md` exists and records any working assumptions.
- If drafting proceeded on working assumptions, the report cover states the context status and the assumed frame.
- Client grouping is confirmed or unresolved files remain in `source-drop/unassigned/`.
- Customer type is resolved as `individual` or `corporate` before drafting.
- Regulatory grounding is source-backed and fresh enough for the operating context.
- Missing policy, stale authority, or unsupported grounding is recorded as a gap.

## Evidence And Analysis

- Every material fact cites document plus page/section plus field/line, with method and confidence.
- Every absence claim includes a search trail.
- Every conflict appears in `conflicts-and-gaps.md` and in the relevant report section.
- Completeness rows are present for PEP/RCA, sanctions/adverse media, tax residency, expected activity, document freshness/expiry, and official-source freshness.
- SOW, SOF, net worth/financial position, and ownership/control reach triangulation and residual uncertainty.
- Corroboration statements are quantified: declared amount, evidenced amount, remainder.
- Corporate ownership maps include every intermediate entity and natural person, with per-layer evidence status.
- Estimates show method, assumptions, and uncertainty.

## Arithmetic And Figures

- Every numeric claim ties to the arithmetic check in `review-bundle/analysis.md`.
- Figure and exhibit counts reconcile with the exhibit register.
- Financial corroboration figure is present when monetary facts exist.
- Corporate reports include an ownership/control diagram when ownership facts exist.
- Screenshots/exhibits cite source, page/section, extraction method, and confidence.
- No report source line cites scripts, pipeline files, or review-bundle paths.

## Risk Module, If Enabled

- Methodology is cited by file and version.
- Every factor input cites the factual record.
- Aggregate score arithmetic is checked.
- Draft banner and compliance-channel note are present.
- Ambiguous or unscorable factors are recorded without inventing assumptions.

## Report Voice And Structure

- Analytical body sentences are about the customer, documents, people, values, or facts — not about the report itself.
- Observation cards include criterion, observed condition, evidence, review significance, and limits.
- Report contains no approval, decline, escalation, condition, next-action, or recommendation language.
- Report is marked internal compliance use only.
- Disclaimer appears on cover and final page:

> Drafted by an AI assistant for review by a qualified compliance professional. Not a regulatory determination, approval, recommendation, or instruction.

## Render Check

- Versioned HTML exists under `client-packs/*/reports/`.
- PDF and screenshot were rendered from `file://` and inspected.
- Page numbers appear.
- Watermark does not obstruct text.
- Headings wrap cleanly.
- Figures, numeric columns, and evidence images are readable.
- Color is not the only status signal.
- Tables fit print or are moved to appendices.
- No mostly blank forced-break pages or broken cards/captions.

## Final Response Contract

When delivery is complete, respond with:

1. Report path and version.
2. Review bundle path.
3. Client pack name and customer type.
4. Render-check result.
5. Counts of material conflicts, gaps, and human-verification items.
6. Risk module status: enabled, disabled, or blocked, with reason.
7. Any unresolved report-critical limitations.
8. Reminder that the report is not an approval, recommendation, or regulatory determination.
