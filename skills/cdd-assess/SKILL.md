---
name: cdd-assess
description: Use when compliance teams need customer due diligence (CDD), KYC, or AML client onboarding assessment from client materials — evidence bundles, regulatory grounding, source-of-wealth/source-of-funds review, UBO mapping, or source-grounded versioned internal HTML reports for human review.
---

# CDD Assess

Own the workflow from onboarding materials to a polished internal HTML CDD assessment report. The report records facts first, then assessment observations. It must not recommend approval, rejection, escalation, conditions, or operational actions.

Never trust parametric knowledge for regulatory requirements. Use supplied compliance materials first; when they are missing, stale, or insufficient, research official primary or high-trust sources and persist the findings before drafting.

## Leading Discipline

The skill produces an **analytical dossier**: a sourced factual record, derivations, conflicts/gaps, observation cards, and a versioned HTML report. The dossier must let a human compliance reviewer understand the customer without reconstructing the work.

Core behavior:

- **Facts before assessment**: record what is known, where it came from, and how reliable it is before making observations.
- **Corroboration ladder**: for each material claim, show assertion, field-level evidence, triangulation/computation, and residual uncertainty.
- **No silent certainty**: mark estimates, weak extraction, conflicts, missing evidence, and stale sources visibly.
- **Inspectable derivations**: SOW, SOF, net worth, expected activity, and UBO maps show inputs, assumptions, method, arithmetic, and confidence.
- **Primary sources over memory**: regulatory grounding comes from supplied policies, official sources, or persisted high-trust research.
- **Human authority stays outside the report**: the report supports review; it does not decide or instruct.

## Bundled Resources

- `references/operating-context-onboarding.md`: first-run concierge intake.
- `references/workspace-format.md`: workspace, client-pack, and review-bundle layout.
- `references/state-machine.md`: resumable case states and status tracking.
- `references/subagent-briefs.md`: specialist pass briefs and merge rules.
- `references/cdd-concepts.md`: portable CDD methodology.
- `references/completeness-checklists.md`: mandatory individual/corporate coverage checks.
- `references/report-composition.md`: corroboration ladder, paragraph shape, citations, gaps, and observation cards.
- `references/research-finding-format.md`: persisted regulatory research format.
- `references/report-rendering.md`: HTML, figures, print, accessibility, and render checks.
- `references/risk-module.md`: optional draft risk assessment under supplied methodology.
- `references/final-self-check.md`: delivery checklist and final response contract.
- `templates/`: starter files for operating context, review-bundle files, and research findings.
- `scripts/`: mechanical validators only; they do not author analytical content.
- `examples/`: miniature examples of desired analytical prose.
- `assets/`: default HTML template, CSS, logo placeholder, and watermark placeholder.

Read the relevant reference only when performing that part of the workflow.

## Authorship Boundary

Reports are **authored from evidence, never generated from configured data**. Scripts and tools are allowed for exactly four jobs: extracting text/images from materials, mechanically recomputing arithmetic, validating bundle/report quality, and rendering/render-checking HTML. Everything else — factual record, derivations, consistency sweep, narrative, observations, gaps, and report HTML content — must be composed by the agent working from extracted evidence.

Do not write a generator script that holds case data and emits reports or review-bundle files. Not for "sample" reports, not for "template testing", not to batch multiple clients, not because the cases look similar. A script cannot notice an anomaly nobody configured into it, so its output is a template demo, not an assessment — if such a demo is ever produced anyway, its cover and version history must label it `template demo — not an assessment`, and it does not count as a report for any purpose in this skill. Every analytical sentence must trace to extracted evidence through the review bundle, and report sources must cite client materials and persisted research only — never pipeline files, scripts, or bundle paths.

## Workflow

### 1. Establish Operating Context

If `OPERATING_CONTEXT.md` is missing, blank, stale, or visibly incomplete, read `references/operating-context-onboarding.md` and run the concierge intake. Create useful workspace state before asking. Ask one focused blocking question at a time and save each answer immediately.

Minimum context:

- compliance officer name, role, team, and represented entity
- jurisdiction(s), regulator(s), and source freshness policy
- client types handled
- internal policies, procedures, checklists, risk methodology, and report expectations
- audience, confidentiality, logo, watermark, and style requirements
- available compliance knowledge pack and known gaps

You may create the workspace, inventory materials, and propose grouping before the context is complete. Do not draft an assessment report before report-critical context exists, unless the officer explicitly directs drafting on working assumptions.

**Completion gate — context ready for analysis:**

- `OPERATING_CONTEXT.md` exists and has no blank report-critical fields; unknowns are marked `to confirm` with status/source notes.
- Represented entity, jurisdiction/regulator frame, source-drop location, and grounding path are known or explicitly assumed by officer direction.
- Current blocker and next step are recorded.

### 2. Create Or Reuse Case Workspace

Read `references/workspace-format.md` and `references/state-machine.md` before creating or changing structure. Preserve the original source drop untouched.

If materials are mixed across multiple clients, infer grouping using folder names, filenames, extracted names, registration numbers, form types, and document text. Ask for confirmation before copying materials into normalized client packs. Put ambiguous files in `source-drop/unassigned/`.

For each client pack, identify customer type before analysis: `individual`, `corporate`, or `unclear`. Resolve `unclear` before report drafting.

**Completion gate — workspace ready:**

- Workspace follows `references/workspace-format.md`.
- `MATERIALS.md` inventories every received file and records grouping plan/status.
- Each client pack has `materials/`, `extracted/`, `review-bundle/`, `reports/`, and `review-bundle/status.md`.
- Review-bundle starter files are created from `templates/`.
- Customer type is confirmed or drafting is blocked.

### 3. Ground The Review

Build or refresh the compliance knowledge base.

Source hierarchy:

1. user-supplied entity policies, procedures, checklists, and risk methodology
2. official regulator, statute, FIU, government, court, or supervisory sources
3. recognized standards bodies such as FATF, Wolfsberg, Basel, IOSCO, or similar
4. secondary sources only for orientation, never final authority

If grounding is missing or stale, browse primary/high-trust sources. Persist each reusable finding using `references/research-finding-format.md` or `templates/research-finding.md`.

**Completion gate — grounding ready:**

- Each requirement used in the report has a supplied-policy citation or persisted research finding.
- Findings include requirement, citation, access date, jurisdiction/scope, interpretation, report implication, uncertainty, and limits.
- Missing internal policies or stale/unavailable authority are recorded as grounding gaps.
- No observation relies on unsupported recall.

### 4. Run Specialist Passes

Read `references/subagent-briefs.md`. Use subagents when supported; otherwise run the same passes sequentially. Preserve raw pass outputs in the review bundle.

Required passes:

- Extraction pass
- Factual record pass
- Regulatory research pass
- Derivation pass
- Arithmetic verification pass
- Consistency sweep
- Completeness pass
- Citation review pass
- Narrative composition pass
- Risk module pass, only when enabled under `references/risk-module.md`
- Report critique pass

For every extracted or derived item, record source file, page/section, method, confidence, assumptions, and reviewer status. Low-confidence OCR/table parsing or ambiguous derivation is `Needs human verification`, not a confirmed fact.

**Completion gate — specialist passes complete:**

- Raw outputs are preserved under marked headings in the matching bundle files.
- Every material fact is represented in `record.md` with field-level citation, method, confidence, and reviewer status.
- Every derivation in `analysis.md` shows inputs, method, arithmetic, assumptions, confidence, and residual uncertainty.
- `analysis.md` contains a mechanical arithmetic check for every numeric claim intended for the report.
- Completeness checklist includes mandatory rows even when facts are `not observed`, with search trails.
- Citation review has flagged and resolved or recorded unsupported claims.

### 5. Produce Review Bundle

Before rendering HTML, produce the four-file review bundle defined in `references/workspace-format.md`:

- `record.md` — factual record with field-level citations, source register, completeness checklist, and search trails
- `analysis.md` — derivations, ownership/control by layer, consistency sweep, and arithmetic check
- `composition.md` — narrative plan, observation cards, section outline, figure plan, critique-pass notes
- `conflicts-and-gaps.md` — materiality-ordered worklist

Resolve contradictions explicitly. Do not hide conflicting source evidence. If no visual evidence artifact is generated for a critical exhibit, record `No visual evidence generated` as a gap with the reason.

**Completion gate — bundle ready for report:**

- `scripts/validate-bundle.py client-packs/*/review-bundle` passes or failures are recorded and justified.
- Every absence claim states where the analyst looked.
- Conflicts and gaps are ordered by factual materiality and include amount-at-stake or affected analysis.
- Corporate ownership maps document every intermediate entity down to natural persons with per-layer evidence status.
- Observation cards contain criterion, observed condition, evidence, review significance, and limits.

### 6. Render Versioned HTML Report

Read `references/report-rendering.md` and `references/report-composition.md`. Copy/adapt the bundled template/CSS into the workspace and render a versioned report, such as `reports/v001-individual-jane-tan-onboarding-assessment.html`.

The template is a starting point, not a fixed schema. Adapt section order, labels, exhibits, page breaks, and layout when user feedback, case materials, or reviewer needs justify it, while preserving mandatory coverage, sourceability, page numbering, render checks, and no decision/action language.

Default report flow:

1. compact dossier header and table of contents
2. reviewer brief with key figures, customer story, evidence strengths, and uncertainties
3. evidence map
4. customer understanding
5. client-type analysis: SOW, SOF, net worth, UBO/ownership/control, plausibility, conflicts
6. evidence exhibits
7. regulatory grounding
8. assessment observations
9. draft risk assessment, only when enabled
10. gaps, human-verification items, review comments
11. version history, appendix fact tables, and disclaimer

Focus most effort on customer understanding and client-type analysis. The body must be readable as prose before the reviewer inspects tables.

**Completion gate — report rendered:**

- HTML filename includes version, customer type, and short customer name.
- Major analytical sections open with sourced prose and name the main uncertainty.
- Report sources cite client materials and persisted research only.
- `scripts/check-banned-language.py` and `scripts/validate-citations.py` pass on the report. If the runtime cannot run Python, record that limitation and hand-check the report against the banned-terms list and citation rules.
- If drafting proceeded on working assumptions, the cover states the context status and the assumed frame.
- Disclaimer appears on cover and final page.

### 7. Render Check And Final Delivery

Run the render check in `references/report-rendering.md` or `scripts/render-check.sh`. Inspect the PDF and screenshot before delivery; the render critique brief is in `references/subagent-briefs.md`. Then run `references/final-self-check.md`.

**Completion gate — delivered:**

- Render-check artifacts were inspected for page numbers, table fit, watermark overlap, figure readability, blank pages, and broken cards/captions.
- `references/final-self-check.md` passes or unresolved failures are listed for human verification.
- `review-bundle/status.md` is advanced to `delivered` only after the final response is sent.
- Final response follows the contract in `references/final-self-check.md`.
