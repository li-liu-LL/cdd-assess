# Report Composition

Use this reference after extraction, derivation, completeness, and citation review. It defines what a finished section is. The finished product is an analytical dossier: for every material claim a reviewer can see what the customer asserted, what the evidence shows at field level, what was computed or triangulated from it, and exactly what remains unproven.

## The Corroboration Ladder

For every material claim — identity, address, occupation and tenure, income, each SOW component, each SOF channel, net worth, each owner and controller, authority, expected activity — climb this ladder and write what each rung produced:

1. **Assertion.** What the customer declared, cited to document, page/section, and field.
2. **Field-level evidence.** Every occurrence of the same fact across sources, down to statement transaction lines, register rows, payroll fields, MRZ lines, and form fields. Line items in bank, exchange, payroll, and register documents are evidence in their own right; read them individually — a closing balance is one fact, each transaction line is another.
3. **Triangulation and computation.** Connect independent evidence to the assertion and show the working: reconcile arithmetic, annualize income, compare earning capacity against declared accumulation and tenure, link transaction lines to declared assets and funding channels, compare dates, ages, tenures, and identifiers across documents. State inputs, method, assumptions, and result.
4. **Residual.** What the evidence still does not show, quantified where possible, and why it matters for review.

A claim analysed only at rungs 1–2 is an inventory entry. The Customer Understanding and Client-Type Analysis sections must reach rungs 3–4 for every material claim.

## Quantification

Every corroboration statement carries its numbers: the declared amount, the independently evidenced amount, the remainder, and what the evidence consists of. Write "SGD 920,000 of the declared SGD 7,780,000 (12%) is visible in institution statements; the remaining SGD 6,860,000 rests on customer declarations", with the components itemized nearby. The same applies to coverage counts: sources that are independent versus customer representations, facts verified versus declared, checklist rows observed versus not observed.

## Mechanical Arithmetic Check

Before the self-check can pass, recompute every numeric claim mechanically and record the result in `review-bundle/arithmetic-check.md`. Cover at minimum:

- component sums for SOW, SOF, net worth, assets, liabilities, capital, and declared funding
- coverage ratios and percentages, including independently evidenced amounts versus declared amounts
- statement reconciliations: opening balance plus listed movements versus closing balance
- ownership percentages, indirect UBO percentages, share counts, and threshold comparisons
- expected-activity arithmetic, such as count multiplied by average ticket versus declared monthly volume
- FX conversions and threshold comparisons, with rate, source or assumption, date, and purpose
- key-figures band metrics, conflict counts, gap counts, source counts, and page/report counts if shown

Use a scratch script when the runtime supports one. The script can be temporary, but the inputs, formulae, and output must be saved or pasted into `arithmetic-check.md`. If no script runtime is available, create a row-by-row arithmetic table and mark it as manual. A high-precision report whose numbers are not mechanically checked has failed composition, even if the prose reads well.

## FX And Threshold Orientation

Do not convert currencies silently. If a report compares a customer amount to a threshold in another currency, cite an official/source-provided FX rate when available. If no rate is supplied and the conversion is used only for threshold orientation, label it as an assumption, state the assumed rate, and keep the conclusion bounded: "exceeds on any reasonable rate" or "requires current-rate confirmation", as appropriate. Do not present assumed FX as a production fact.

## Consistency Sweep

Before composing, sweep every extracted value across all documents and account for each anomaly. Compare at minimum:

- names, including MRZ and surname/given-name order on identity documents
- identifiers (national ID, passport, registration numbers) and their cross-references between documents
- dates: birth, incorporation, signatures, statement periods, expiries, register entries
- addresses, unit numbers, and postal codes
- contact details, including email-domain versus stated employer or entity name
- monetary values, percentages, share counts, and their arithmetic
- tenures and ages against dates (years in employment versus DOB, experience versus incorporation date)
- declared expected activity against ticket size, transaction count, monthly volume, product scope, and relationship purpose
- declared screening, PEP/RCA, tax-residency, and source-of-wealth statements against actual artifacts present in the pack

Record the sweep in `review-bundle/composition.md` as a `## Consistency sweep` list: each check performed and its outcome (`consistent`, or the anomaly found). Every anomaly then appears in the report — analysed in the relevant narrative with its evidence, and, if unresolved, logged as a conflict or human-verification item. An anomaly that appears nowhere is a composition defect.

## Absence Claims And Search Trail

Every absence claim must say where the analyst looked. Do not write only "not observed", "not provided", or "not performed". Write the search trail:

- "No sanctions/PEP screening output observed after checking S1 section 5, all seven source files, and `client-packs/.../materials/` filenames."
- "No BVI formation document observed after checking the UBO declaration, registry extract, annual return, and all corporate materials."
- "No expected transaction volume observed after checking the onboarding form relationship-purpose section, product acknowledgement, and source-of-funds declaration."

The search trail belongs in the completeness checklist, conflicts/gaps table, and any report sentence that relies on the negative fact. Absence claims without search trails fail composition because the reviewer cannot tell whether the analyst searched or merely did not notice.

## Gaps And Materiality Ordering

The gaps and human-verification table is a factual worklist, not a recommendation list. Sort gaps by review materiality within each report section, with conflicts first when they affect identity, legal existence, ownership/control, SOW/SOF, expected activity, or screening integrity.

Each row includes:

- **ID**: conflict/gap identifier that does not collide with source IDs.
- **Item**: concise issue name.
- **Amount at stake / affected analysis**: amount, percentage, ownership leg, identity field, screening scope, or baseline element affected. Use `not monetary` only when no amount or percentage is involved.
- **Evidence state**: what is observed, what is missing, and whether the missing item is independent evidence, customer representation, or system output.
- **Search trail**: where the absence or conflict was checked.
- **Sources**: field-level citations.
- **Status**: `needs human verification`, `evidence limitation`, `baseline gap`, or similar neutral wording.

Do not hide a material monetary or ownership gap behind lower-impact spelling, style, or administrative gaps. Materiality ordering does not decide the case; it helps the reviewer see the factual weight of unresolved items.

## Paragraph Shape

Analytical paragraphs run: claim → strongest evidence, cited at field level → computed or triangulated support → conflict or limitation → why it matters for review. Each SOW, SOF, net-worth, and ownership/control subsection gets two to three such paragraphs plus a supporting table or figure. Orientation sections (reviewer brief, evidence map, customer understanding) open with three to six sentences of sourced prose before any table.

Tables carry inventories, comparisons, calculations, ownership lists, gaps, and appendices. The narrative must stand on its own if every table were removed; the tables must reconcile with the narrative if every paragraph were removed.

## Voice

The grammatical subject of nearly every sentence is the customer, a person, a document, a value, or a fact: "The declared property wealth of SGD 4,300,000 rests on…", "The bank statement records a rental credit…". Sentences whose subject is "the report", "this assessment", or "the dry run" belong only in Review Comments, Version History, and scope notes — nowhere in the analytical body.

Use neutral review language: `observed`, `not observed`, `supported by`, `not corroborated by`, `inconsistent with`, `evidence limitation`, `review significance`, `needs human verification`.

Avoid decision and instruction language: `approve`, `reject`, `decline`, `escalate`, `must obtain`, `should request`, `recommended`, `condition precedent`, `next steps`, `remediate`, `acceptable`, `unacceptable`.

If an entity policy or regulatory source itself contains decision-flavored words, quote or paraphrase it only as an attributed criterion and keep the report's own voice neutral. For example, a policy phrase containing "not acceptable" may appear as a cited policy criterion, but the observation and significance fields still use `not corroborated`, `evidence limitation`, or `needs human verification`.

## Citations

Inline citations resolve to document plus page/section plus field or line:

- `[S1 §3 field "Estimated Net Worth"]`
- `[S5 p.1 txn 2026-01-10 "Property Rental – Sentosa"]`
- `[C7 row "Kevin Ng Jia Rong"]`
- `[C9 MRZ]`

Bare `[S1]` is acceptable only for whole-document statements (that a document exists, its date, its type). Ranges such as `[S1-S8]` do not appear in the analytical body; list the specific sources that carry the point.

Define one source register per client pack before drafting. Default to `S1`, `S2`, ... for source documents in every per-client report unless the operating context supplies another convention. Do not reuse source IDs as conflict, gap, or observation IDs; use distinct prefixes such as `CON1`, `G1`, and `OC1`.

Screening declarations are not screening results. Treat a customer or entity declaration about PEP/sanctions/adverse-media status as declaration data only. A screening result requires a screening-system output, search artifact, or documented screening source; if none exists, record `not performed` or `not observed` with the search trail.

## Derivation Write-Ups

Write a separate subsection for each of:

- **Source of Wealth** — how wealth appears to have accumulated over time, component by component, each with its own corroboration ladder.
- **Source of Funds** — where relationship or transaction funding appears to come from, traced through observed transaction flows where statements permit.
- **Net Worth / Financial Position** — declared values, corroboration arithmetic, coverage ratio, and unsupported components itemized.
- **Ownership and Control** — natural persons, direct and indirect holdings, control roles, nominee or bearer-share indicators, capital history where registers permit, and the UBO method applied.

Each derivation shows inputs, method, assumptions, confidence, corroboration, and unresolved limits. Phrase findings as observed support or limitation, not as approval or action.

## Multi-Tier Ownership Coverage

Corporate ownership analysis must document every layer from the legal customer down to natural persons. Do not collapse an intermediate entity into a single note.

For each layer and owner/controller, record:

- legal name, customer/entity/person type, jurisdiction, and role
- direct percentage at that layer and calculated indirect percentage in the customer
- source evidence for the layer: register row, declaration, formation document, trust deed, board record, passport/ID, or `not observed`
- verification status for the intermediate entity and for the natural person separately
- control roles that are not ownership: director, signatory, settlor, trustee, protector, manager, nominee, authorised trader
- threshold method applied and whether the person is above, below, or otherwise relevant despite being below threshold

Every intermediate entity must have its own evidence status. Every natural person above the applicable threshold must have identity evidence status. If an intermediate entity, ownership link, or natural-person ID is declaration-only, show that layer as declaration-only and carry it to gaps if unresolved.

## Observation Cards

Use observation cards for assessment observations:

- **Criterion**: internal policy, regulatory requirement, or source-grounded principle.
- **Observed condition**: what the materials show or do not show.
- **Evidence**: source IDs at field level, extraction method, confidence, and corroboration.
- **Review significance**: why it matters for customer understanding, monitoring baseline, ownership/control, SOW/SOF plausibility, or evidence quality.
- **Limits**: evidence limitations, unresolved conflicts, stale sources, and assumptions.

Do not include recommendation, decision, escalation, required action, approval, decline, or condition language.
