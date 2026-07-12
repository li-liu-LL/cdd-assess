# Report Structure

The report is a complete onboarding assessment: document review, gap analysis, risk assessment, and a draft recommendation for compliance sign-off, in a single document. Each part answers a named compliance question; open each part's narrative by answering its question, then show the evidence.

Entity-specific items — the entity's name, its CDD/onboarding form name and sections, its product set, and its AML questionnaire policy — come from `OPERATING_CONTEXT.md`, never hardcoded. Composition discipline (corroboration ladder, citations, search trails, arithmetic checks) still follows `references/report-composition.md`; risk scoring and the recommendation follow `references/risk-and-recommendation.md`.

Decision and action language (ratings, EDD triggers, conditions, the recommendation) is confined to Part A's executive summary table and Part I, inside decision-zone markers per `scripts/check-decision-language.py`. Parts B–H stay in neutral evidence voice.

Each part's closing compliance assessment follows the observation-card discipline from `references/report-composition.md` — criterion, observed condition, evidence, review significance, limits — in place, within that part. There is no separate consolidated observations section.

## Individual Clients

The structure is corporate-shaped; for individual customers, adapt rather than force-fit, and never silently drop a section — a section that does not apply states `Not applicable — individual customer` with the basis:

- **5 Customer Profile** — identity, capacity (principal/agent), occupation, and address facts replace corporate information.
- **6 Nature of Business** — becomes occupation, income sources, and economic activity; the assessment questions still apply (activity explained, understood).
- **7 Ownership and Control** — usually `not applicable`; assess capacity and any agent/attorney authority instead. Keep the section if the individual acts through vehicles.
- **8 Licensing** — assess only if the individual's own activity may be regulated (e.g., professional intermediary); otherwise `not applicable` with the basis.
- **12 AML Controls** — usually `not applicable` unless the individual is an intermediary.
- **15 CDD Form Completeness** — review against the entity's individual form sections from `OPERATING_CONTEXT.md`.
- Directors, authorised representatives, and platform-user assessments collapse into the capacity/authority assessment.

Parts A, B, E, F(13), G(14), H, and I apply to individuals unchanged.

## Part A — Executive Summary

**1. Executive Compliance Summary.** One table: customer name, jurisdiction of incorporation, customer type, industry, UBOs identified (yes/no), directors verified (yes/no), licensing review completed (yes/no), SOW assessment (satisfactory / incomplete / unsatisfactory), SOF assessment (same scale), AML questionnaire required (yes/no), overall risk rating, EDD required (yes/no), recommendation. Every row's value must reconcile with the section that derives it; the summary never introduces a finding the body does not support.

**2. Key Findings.** Three short cited lists: key strengths, key risks, key outstanding items. Each bullet cites its supporting section or register reference.

## Part B — Information Sources and Evidence Review

*Question: what evidence do we have, and how reliable is it?*

**3. Documents Reviewed.** The source register as a document inventory: document, date, status.

**4. Evidence Quality Assessment.** Reliability tiers per source type (government registry, audited financials, customer declarations, website, internal charts), consistent with the source reliability ladder in `references/cdd-concepts.md`.

## Part C — Customer Understanding Assessment

*Questions: who is the customer, and do we sufficiently understand its business and operations?*

**5. Customer Profile Assessment.** Corporate/individual information and history: legal name, registration, addresses, website, contacts, incorporation, corporate changes, group structure.

**6. Nature of Business Assessment.** Information obtained (CDD form, website, financials, supporting documents), then an assessment table: products/services explained, revenue model explained, customer base identified, geographic markets identified, virtual-asset activities explained, business operations understood — each yes/no with evidence. Close with an express compliance assessment: whether the entity has sufficient understanding of the customer's business, whether additional information is required, and whether proposed activities align with the stated business model. Where information is insufficient, generate the clarification questions into the Clarification Register (Part H).

**7. Ownership and Control Assessment.** Shareholding structure, UBO assessment, directors, authorised signatories, authorised platform users, and a control determination: who owns, who controls, whether nominee arrangements exist, whether ownership and control are fully understood. Multi-tier coverage rules in `references/report-composition.md` apply.

## Part D — Regulatory and Product Assessment

*Questions: are any activities regulated with licences evidenced, and why does the customer need the entity's products?*

**8. Regulatory and Licensing Assessment.** Business activity review against regulated-activity categories (payment services, money transmission, e-money, virtual asset services, custody, remittance, financial advisory, other), each grounded in supplied policy or persisted research — never memory. Licensing assessment table: regulated activities identified, licensing potentially required, licence provided, licence valid, independent verification completed. Licensing gap analysis: licences expected, provided, missing, clarifications required (routed to the registers). Close with whether the regulatory status is adequately understood.

**9. Intended Relationship and Product Use Case Assessment.** Intended products/services, wallet/fiat/crypto usage from the CDD form. Transaction profile table: expected monthly volume, monthly transactions, daily withdrawal limits, wallet addresses, transaction purpose — provided/missing each. Commercial rationale: why the customer requires the entity's services, how they fit its operations, whether proposed usage is commercially reasonable and consistent with the business model.

## Part E — Source of Wealth and Source of Funds Assessment

*Question: do we adequately understand and verify SOW and SOF?*

**10. Source of Wealth Assessment.** Information provided, supporting documents, corroboration ladder per component, assessment table (narrative provided, documents provided, accumulation explained, consistency with business activities), and a conclusion: satisfactory / partially satisfactory / unsatisfactory, with the quantified corroboration figures.

**11. Source of Funds Assessment.** Expected sources (operating revenue, shareholder funding, group funding, investment proceeds, virtual assets), assessment table (narrative, documents, funding accounts identified, wallet sources identified, funds flow understood). Customer funds determination: whether funds originate from the company's own funds, its customers, or third parties. AML questionnaire trigger table: receives customer funds, acts as intermediary, holds customer assets → AML questionnaire required yes/no per the entity's policy in `OPERATING_CONTEXT.md`. Close with adequacy of SOF information.

## Part F — AML/CFT Assessment

*Question: does the customer present AML/CFT, sanctions, regulatory, or reputational risks?*

**12. AML Controls Assessment** (where customer funds, regulated business, or intermediary activity apply): AML governance, customer onboarding, sanctions screening, PEP screening, transaction monitoring, STR reporting — what the customer evidences about its own controls.

**13. Screening Assessment.** Sanctions, PEP, and adverse-media screening with a results summary. Declarations are not screening results; apply the screening rules in `references/report-composition.md`. The agent performs open-web adverse-media research only when the user has explicitly enabled it (in `OPERATING_CONTEXT.md` or for the case); such results are labelled `agent web research` and never presented as screening-system results. Absent system screening remains a gap either way.

## Part G — Documentation Review and Gap Analysis

*Question: have all required information and documents been obtained?*

**14. Documentary Completeness Assessment.** Jurisdiction-specific requirements matrix (required document, received, status, acceptable alternative), grounded in supplied policy or persisted research. Deficiencies categorized: missing, expired, inconsistent, requiring refresh.

**15. CDD Form Completeness Assessment.** Section-by-section review of the entity's CDD form (account purpose, product selection, transaction profile, withdrawal limits, SOW/SOF, directors, authorised representatives, authorised platform users, declaration and sign-off — adapt to the actual form): complete/incomplete with comments.

## Part H — Outstanding Matters Register

**16. Outstanding Information Register.** Generated from the CDD form review and the business, licensing, and SOW/SOF assessments: ref, information required, reason, priority.

**17. Outstanding Documents Register.** Generated from the documentary review: ref, document required, reason, priority.

**18. Clarification Register.** Customer-facing clarification questions generated wherever a section found insufficient information: ref, clarification required, priority.

Register rows live in `review-bundle/conflicts-and-gaps.md` first and render from there; every row carries its search trail and source citations. Every condition precedent in Part I must reference a register row.

## Part I — Risk Assessment and Recommendation

*Question: based on the overall assessment, can the customer be onboarded, and under what conditions?*

This part follows `references/risk-and-recommendation.md` and sits inside decision-zone markers.

**19. Risk Assessment.** Factor table — jurisdiction, industry, product, licensing, ownership, SOW, SOF, AML/CFT, documentation — each with rating and cited rationale; overall risk rating on the five-band scale with the aggregation shown.

**20. Enhanced Due Diligence Assessment.** EDD trigger table (PEP exposure, high-risk jurisdiction, customer funds, virtual-asset activities, licensing concerns, complex ownership) and the EDD-required determination.

**21. Final Compliance Recommendation.** Conditions precedent (each referencing a register row), the recommendation (approve / conditional approval / escalate for EDD / reject / pending information), and the compliance rationale narrative covering business understanding sufficiency, regulatory and licensing outcome, SOW/SOF adequacy, AML/CFT considerations, outstanding risks and mitigants, and the basis for the recommendation. The section opens with the draft-for-signoff banner.

## Apparatus

The dossier apparatus from `references/report-rendering.md` still applies: compact header, table of contents, key-figures band (in Part A), exhibit register, figures, appendix fact tables, version history, review comments, and the disclaimer on cover and final page.
