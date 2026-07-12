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
- Licensing assessment covers the regulated-activity categories with grounded category calls and a licensing gap analysis.
- Product use-case assessment covers transaction profile, commercial rationale, and the customer funds determination with AML questionnaire triggers.
- CDD form completeness is reviewed section by section, and every incomplete section has a register row.
- The three outstanding-matters registers are populated from the assessments, each row tracing to a gap, conflict, or checklist absence.
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

## Risk Assessment And Recommendation

- Methodology is identified: supplied (cited by file and version) or built-in default (stated as such, with the entity-methodology gap in the Outstanding Information Register).
- Every factor input cites the factual record; unscorable factors carry search trails, not invented assumptions.
- Aggregation arithmetic and factor counts are in the arithmetic check.
- EDD trigger table is present with per-trigger evidence.
- Every condition precedent references an outstanding-matters register ref.
- Exactly one recommendation option is selected; the rationale covers business understanding, licensing outcome, SOW/SOF adequacy, AML/CFT considerations, outstanding risks and mitigants, and the basis for the recommendation.
- Every executive-summary row reconciles with the body section that derives it.
- Draft-for-signoff banner opens Part I; compliance-channel note is present.

## Report Voice And Structure

- Analytical body sentences are about the customer, documents, people, values, or facts — not about the report itself.
- Each part's closing compliance assessment follows the observation-card discipline: criterion, observed condition, evidence, review significance, and limits.
- Decision language (ratings, EDD determinations, conditions, recommendation) appears only inside the executive-summary and Part I decision zones; `scripts/check-decision-language.py` passes.
- The report nowhere states that the customer is approved, rejected, or onboarded — the recommendation is framed as a draft pending officer approval.
- Report is marked internal compliance use only.
- Disclaimer appears on cover and final page:

> Drafted by an AI assistant. The risk rating and recommendation are draft proposals requiring review and approval by a qualified compliance officer before any onboarding action. Not a regulatory determination.

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
5. Counts of material conflicts, gaps, register items, and human-verification items.
6. Draft overall risk rating, EDD determination, and recommendation — stated as drafts pending compliance officer approval.
7. Any unresolved report-critical limitations.
8. Reminder that the rating and recommendation are drafts and the compliance officer's documented sign-off is the decision.
