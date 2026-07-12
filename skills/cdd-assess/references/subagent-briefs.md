# Subagent Briefs

Use these briefs when the runtime supports subagents. If it does not, run the same passes sequentially and preserve the same outputs. The lead agent owns final synthesis and report authorship.

## Merge Rules

- Preserve raw pass output under marked headings in the matching review-bundle file.
- Synthesized conclusions must cite extracted items, client materials, or persisted research.
- If passes conflict, record the conflict in `conflicts-and-gaps.md`; do not silently choose.
- Do not let a subagent write final analytical report prose unless the lead agent reviews every claim against the bundle.
- Subagents may use scripts only for extraction, arithmetic, validation, or rendering checks — never to generate analytical case content.

## Extraction Pass

Mission: extract factual content from assigned materials without assessment.

Inputs: `client-packs/*/materials/`, existing source register if present.

Append raw output to: `review-bundle/record.md` under `## Raw extraction pass`.

Required per item: source ID, file, page/section/row/field/line, extracted value, extraction method, confidence, ambiguity, reviewer status.

Do not infer missing facts, summarize away transaction lines, or assess significance.

## Factual Record Pass

Mission: classify customer type and structure extracted facts into the individual or corporate factual record.

Append raw output to: `review-bundle/record.md` under `## Raw factual record pass`.

Required: identity/legal existence, addresses, people, ownership/control, financial facts, relationship purpose, expected activity, screening declarations/results, document freshness, and mandatory `not observed` rows with search trails.

## Regulatory Research Pass

Mission: ground applicable requirements using supplied policies first, then official/high-trust sources.

Append raw output to: `knowledge/research/*.md` using `references/research-finding-format.md`; summarize in `review-bundle/composition.md` under `## Regulatory Grounding Pass`.

Required: requirement, citation, access date, jurisdiction, interpretation, report implication, uncertainty, and limits.

## Licensing Assessment Pass

Mission: assess whether the customer's activities may constitute regulated activities (payment services, money transmission, e-money, virtual asset services, custody, remittance, financial advisory, other) and whether licences are evidenced. Ground every category call in supplied policy or persisted research, never memory.

Append output to: `review-bundle/analysis.md` under `## Licensing Assessment`.

Required per category: indicators observed with citations, grounding reference, licence provided/valid/independently verified status, and the licensing gap analysis (expected, provided, missing, clarifications routed to the registers).

## Product Use-Case Pass

Mission: assess the intended relationship, product usage, transaction profile, and commercial rationale against the customer's stated business model, using the entity's CDD form and product set from `OPERATING_CONTEXT.md`.

Append output to: `review-bundle/analysis.md` under `## Product Use Case And Transaction Profile` and `## Customer Funds And AML Questionnaire Triggers`.

Required: intended products/services, wallet/fiat/crypto usage, transaction profile items marked provided/missing, commercial rationale, customer funds determination (own / customers' / third-party), and AML questionnaire trigger results.

## Derivation Pass

Mission: derive SOW, SOF, net worth/financial position, expected activity plausibility, and UBO/ownership/control maps.

Append raw output to: `review-bundle/analysis.md` under `## Raw derivation pass`.

Required: inputs, method, assumptions, calculations, confidence, corroborated amount, residual amount, unresolved conflicts, and per-layer ownership evidence status.

## Arithmetic Verification Pass

Mission: mechanically recompute every numeric claim intended for the report.

Append output to: `review-bundle/analysis.md` under `## Arithmetic check`.

Required: input table, formula, computed result, report claim checked, pass/fail status. Include totals, residuals, coverage ratios, FX conversions, ownership percentages, expected-activity arithmetic, counts, and figure/register counts.

## Consistency Sweep Pass

Mission: cross-check every extracted value across documents per `references/report-composition.md` — names and MRZ order, identifiers, dates, addresses, contact details, values, tenures.

Append output to: `review-bundle/analysis.md` under `## Consistency Sweep`.

Required per check: check performed, sources compared, outcome, conflict/gap ID for each anomaly, notes. Record every check, not only anomalies; route each anomaly into `conflicts-and-gaps.md`.

## Completeness Pass

Mission: apply `references/completeness-checklists.md` for the confirmed customer type.

Append output to: `review-bundle/record.md` under `## Completeness Checklist`.

Required: every mandatory row present even when facts are `not observed`; each absence row carries a search trail stating where the analyst looked.

## Citation Review Pass

Mission: verify every material fact and observation has a field-level citation.

Append output to: `review-bundle/composition.md` under `## Citation Review Pass`.

Flag: bare citations, source ranges, missing page/section/field/line references, unsupported absence claims, report text citing scripts or bundle paths, and confidence missing from exhibits.

## Narrative Composition Pass

Mission: compose analytical prose that climbs the corroboration ladder for every material claim, per `references/report-composition.md`; calibrate against `examples/strong-paragraphs.md`.

Append output to: `review-bundle/composition.md` — reviewer brief plan, section outline, narrative paragraph plan, and observation cards under their template headings.

Required per paragraph-plan row: claim, strongest evidence, computation/triangulation, residual/limit, citations. Observation cards carry criterion, observed condition, evidence, review significance, and limits. The lead agent reviews every claim against the bundle before it enters report HTML.

## Risk And Recommendation Pass

Mission: apply `references/risk-and-recommendation.md` — score each factor from the factual record (supplied methodology first, built-in default otherwise), assess EDD triggers, generate conditions precedent from register rows, and draft the recommendation with its rationale.

Append output to: `review-bundle/analysis.md` under `## Risk Assessment` and `## EDD Triggers`; rationale and conditions to `review-bundle/composition.md` under `## Recommendation Rationale Plan`.

Required: methodology identification (default or supplied file/version), factor table with field-level input citations, aggregation arithmetic (included in the arithmetic check), EDD trigger table, exactly one recommendation option, every condition referencing a register ref, unscorable factors with search trails. All output is draft for compliance sign-off.

## Report Critique Pass

Mission: critique the draft report for completeness, clarity, evidence design, decision-language containment (decision terms only inside the executive summary and Part I decision zones), executive-summary reconciliation with the body, and conditions tracing to register refs.

Append output to: `review-bundle/composition.md` under `## Report Critique Pass`.

Required: issue, location, severity, correction needed, and whether fixed.

## Render Critique Pass

Mission: inspect PDF and screenshot render artifacts.

Append output to: `reports/review-comments.md` or `review-bundle/composition.md` under `## Render Critique Pass`.

Required: page numbers, table fit, figure readability, watermark overlap, heading wraps, blank pages, card/caption breaks, screenshot legibility, disclaimer presence.
