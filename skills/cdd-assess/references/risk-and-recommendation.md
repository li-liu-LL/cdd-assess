# Risk Assessment And Recommendation

Part I of every report drafts a customer risk rating, an EDD determination, conditions precedent, and an onboarding recommendation — as **draft proposals for a qualified compliance officer's review and approval**, never as determinations. The draft-for-signoff banner opens the section:

> *Draft risk rating and recommendation prepared by an AI assistant for review and approval by a qualified compliance officer. No onboarding action may be taken on this document alone.*

All Part I content sits inside decision-zone markers (`<!-- decision-zone: start -->` / `<!-- decision-zone: end -->`) so `scripts/check-decision-language.py` can verify decision language appears nowhere else.

## Framework Selection

The skill is entity- and jurisdiction-neutral. The risk methodology, SOW/SOF rating criteria, EDD trigger list, and AML questionnaire policy come from the user, in this order:

1. **Supplied first.** If a written framework exists in `knowledge/supplied/` (factor definitions, weights, tier boundaries, rating criteria), apply it exactly, citing it by file and version. Ambiguous definitions are scored under both readings side by side, recorded as a gap.
2. **Ask before defaulting.** If a framework is missing, ask the user for it — obtaining the entity's methodology and criteria is part of building the business context, like the operating-context intake. Do not draft Part I or the executive-summary ratings while the question is open.
3. **Built-in defaults only on explicit instruction.** Apply the default framework or default rating criteria below only when the user explicitly directs it. Never adopt a default silently.

When a built-in default is used, the report discloses it prominently: the methodology line names the built-in default framework, states that it is not an entity methodology, and notes that supplying the entity's own methodology or criteria replaces it in the next report version. Record obtaining the entity framework in the Outstanding Information Register.

Whatever the framework source, every factor input cites the factual record at field level. A factor with no recorded input is `not scorable — input not observed`, with the search trail; do not fill inputs from assumptions.

## Default Risk Framework

Nine factors, each rated Low / Medium / High with a one-paragraph cited rationale:

| Factor | Rate on | Indicative High |
|---|---|---|
| Jurisdiction | Incorporation, operations, and UBO jurisdictions against FATF lists and persisted research — cite the finding, never memory | FATF black/grey list, sanctioned, or secrecy jurisdiction in the chain |
| Industry | Stated and observed business activity | Cash-intensive, gambling, arms, shell-like, or opaque activity |
| Product | Products/services requested and transaction profile | High-velocity crypto↔fiat, third-party payments, unhosted-wallet flows at scale |
| Licensing | Part D licensing assessment | Likely-regulated activity with no licence evidenced |
| Ownership | Part C ownership/control assessment | Unresolved UBOs, nominee indicators, bearer shares, layers without evidence |
| SOW | Part E corroboration outcome | Declared wealth substantially uncorroborated or implausible against profile |
| SOF | Part E funds analysis | Funds flow not understood, unidentified third-party or customer funds |
| AML/CFT | Screening results and (where applicable) customer's own controls | Screening hit, PEP without mitigation, absent controls where required |
| Documentation | Part G completeness | Core identity/legal-existence documents missing or expired |

**Overall rating** on five bands — Low / Medium-Low / Medium / Medium-High / High — by default rule:

- any factor High → overall at least Medium-High; two or more High → High
- no High and three or more Medium → Medium
- no High and one or two Medium → Medium-Low
- all Low → Low

Show the rule applied and the count arithmetic in the arithmetic check. A supplied methodology's aggregation rule replaces this one.

## Default SOW/SOF Rating Criteria

Used only under the framework-selection rule above. Rate the executive-summary SOW and SOF rows as:

- **Satisfactory** — narrative and supporting documents present, material components independently corroborated, and the account is plausible against the customer's profile and business activities.
- **Incomplete** — narrative or key supporting documents missing, or a material declared amount remains uncorroborated after the corroboration ladder.
- **Unsatisfactory** — evidence contradicts the declared narrative, or corroboration attempts failed on material components.

State the criteria applied (supplied or default) wherever the rating appears, and keep the quantified corroboration figures next to the rating.

## EDD Assessment

Trigger table, each row present/absent with citation: PEP exposure, high-risk jurisdiction, customer funds involvement, virtual-asset activities, licensing concerns, complex ownership. Any trigger present → `EDD Required: Yes`. A supplied EDD policy overrides this trigger list.

## AML Questionnaire Trigger

From Part E's customer funds determination: receives customer funds, acts as intermediary, or holds customer assets → AML questionnaire required, per the entity's policy named in `OPERATING_CONTEXT.md`. If no policy is supplied, apply the three triggers as the default and record the policy gap.

## Conditions Precedent

Generate conditions from identified deficiencies. **Every condition references an Outstanding Matters Register row** (Part H) — a condition with no register row behind it is a composition defect. Typical conditions: completion of outstanding CDD-form sections, submission of outstanding documents, resolution of ownership/control clarifications, completion of the licensing review, completion of SOW/SOF verification, completion of the AML questionnaire where triggered, wallet ownership verification, completion of sanctions/PEP/adverse-media screening.

## Recommendation

Exactly one of: **Approve / Conditional Approval / Escalate for EDD / Reject / Pending Information.**

Default decision rules (a supplied policy overrides):

- **Pending Information** — outstanding register items prevent assessing a core area (identity, ownership, licensing, SOW/SOF, screening) at all.
- **Reject** — only on an entity-policy prohibition or supplied-policy rule that the evidence squarely meets, cited to that policy. The default framework never generates Reject on its own; absent such a policy rule, use Escalate for EDD.
- **Escalate for EDD** — any EDD trigger present, or overall rating Medium-High or High.
- **Conditional Approval** — no EDD triggers, overall rating Medium or lower, but open register items exist; conditions precedent listed.
- **Approve** — no EDD triggers, no material open register items, overall rating Low or Medium-Low.

## Compliance Rationale

A concise cited narrative covering: sufficiency of business understanding, regulatory and licensing outcome, adequacy of SOW/SOF information, AML/CFT considerations, outstanding risks and mitigants, and the basis for the recommendation. The rationale references sections and register rows; it introduces no new facts.

## Boundaries

- The rating and recommendation are drafts; the compliance officer's documented approval is the decision. The report never states that the customer *is* approved, rejected, or onboarded.
- Risk tier, factor scores, and screening-derived inputs are compliance-channel content: *"Compliance channel only — do not excerpt into client-facing or sales-facing material."*
- Aggregate arithmetic, factor counts, and threshold comparisons go in the arithmetic check in `review-bundle/analysis.md`.
- When the default framework is used, say so in the report; do not present it as the entity's methodology.
