# Risk Assessment Module (Optional)

An optional report section that drafts a customer risk assessment **strictly under the entity's own supplied methodology**. It extends the factual dossier; it never replaces or reorders it.

## Activation Gate

Enable this module only when both are true:

1. `OPERATING_CONTEXT.md` lists `risk-assessment` under `## Report Modules`.
2. A written risk methodology exists in `knowledge/supplied/` (scoring model, factor definitions, weights, tier boundaries) or in an officer-confirmed official source persisted under `knowledge/research/`.

If either is missing, do not score. Record in the report's regulatory grounding section: "Risk assessment module not enabled: no supplied methodology observed" with the search trail. Never substitute a methodology from model memory — a generic FATF-style factor list is not a scoring methodology.

## What The Module Produces

A report section titled "Draft Risk Assessment (per {methodology name and version})", placed after Assessment Observations, containing:

1. **Methodology line**: name, version/date, and file citation of the supplied methodology; any factors the methodology defines that could not be scored, with reasons.
2. **Factor table**: one row per factor the methodology defines — factor, input facts (field-level citations into the factual record), the methodology rule applied (cited to the methodology document's section), resulting factor score, and confidence in the inputs.
3. **Draft aggregate**: the aggregate score/tier computed exactly per the methodology's aggregation rule, shown with its arithmetic. Include in the arithmetic check.
4. **Sensitivity note**: when unresolved gaps or conflicts could move any factor enough to change the tier, name which gaps and which direction. This is factual ("G2 unresolved: if investor capital is third-party, the ownership factor moves from X to Y"), not advisory.
5. **Draft banner**: the section opens with — *"Draft scoring under {methodology vX} for reviewer validation. Not a risk determination."*

## Boundaries

- **Inputs come from the factual record only.** Every factor input cites the record; a factor with no recorded input is `not scorable — input not observed`, with the search trail. Do not fill factor inputs from assumptions.
- **The methodology is applied, not improved.** If a factor definition is ambiguous, record the ambiguity as a gap and score both readings side by side rather than choosing silently.
- **Decision language stays banned.** The module outputs a draft score and its workings. No approve/decline/escalate/condition/EDD-instruction language — even when the methodology document itself frames tiers as triggering actions, report the tier and cite the methodology's trigger text; do not instruct.
- **Confidentiality**: risk tier, factor scores, and screening-derived inputs are compliance-channel content. The module section carries the note: *"Compliance channel only — do not excerpt into client-facing or sales-facing material."*

## Requirement Evidence Map (bridge input)

When the module is enabled, the regulatory grounding section upgrades to a requirement-by-requirement evidence map: one row per requirement from the supplied checklist or grounded sources — requirement (cited), evidence present (field-level citations), evidence absent (with search trail). Factor inputs in the factor table reference these rows, so the scoring is traceable to the same evidence base as the rest of the report.
