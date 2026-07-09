# Completeness Checklists

Use this reference before rendering HTML. Include every mandatory row in the review bundle and report, even when the value is `not observed`, `not provided`, `not performed`, or `needs human verification`.

## All Reports

| Area | Mandatory coverage |
|---|---|
| Customer type | individual / corporate / unclear; unclear blocks report drafting |
| Operating context | entity, jurisdiction, regulator, reviewer role, source freshness policy |
| Source inventory | document name, version/date, extraction method, confidence |
| Official-source freshness | current / stale / not production-current / inaccessible |
| Screening | sanctions, PEP/RCA, adverse media, and whether screening was performed or only declaration data was observed |
| Tax residency | jurisdiction(s), TIN/registration number, source |
| Expected activity | purpose, products/services, expected transaction count/volume/value where available |
| Arithmetic check | the arithmetic check in `review-bundle/analysis.md` recomputes every report number and key figure |
| Absence search trail | every `not observed` / `not provided` / `not performed` row states where it was looked for |
| Gap materiality | conflicts/gaps table includes amount-at-stake or affected-analysis column and is ordered by factual materiality |
| Document freshness | expiry dates and dated-document age where extractable |
| Evidence artifacts | visual artifact present, or explicit `No visual evidence generated` gap |
| No decision language | no approval, rejection, escalation, condition, or action recommendation |

## Individual Reports

| Area | Mandatory coverage |
|---|---|
| Identity | full name, aliases if any, DOB, nationality, ID number/type, expiry |
| Address | declared address, proof source, freshness |
| Capacity | principal / agent / unclear |
| Occupation | employment/business, role, industry, tenure where available |
| Financial profile | income, assets, liabilities, net worth, investment experience/objective |
| SOW/SOF | declared sources, corroborating evidence, derivations, confidence |
| DPT / product suitability facts | product acknowledgement, experience, existing exposure where applicable |

## Corporate Reports

| Area | Mandatory coverage |
|---|---|
| Legal existence | name, registration number, legal form, incorporation date, status |
| Address | registered address, principal/business address, conflicts |
| Authority | board resolution, authorised signatories/users, authority source |
| Business activity | stated activity, industry, countries of operation where available |
| Ownership/control | shareholders, UBOs, controllers/directors, thresholds/method used |
| Financial profile | revenue, assets, liabilities, net assets, audited/unaudited status |
| SOW/SOF | business profits, investor capital, revenue, asset sources, confidence |
| Multi-tier ownership | each intermediate entity documented down to natural persons, with per-layer evidence and verification status |
