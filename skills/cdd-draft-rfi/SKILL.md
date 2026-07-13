---
name: cdd-draft-rfi
description: Draft a client-facing request-for-information (RFI) email and request schedule from compliance-officer-reviewed CDD report findings. Use after a qualified compliance officer has documented the disposition of a delivered CDD/KYC/AML assessment and approved specific outstanding information, document, or clarification items for client follow-up. Produces versioned drafts and internal traceability; never sends messages or invents requests.
---

# CDD Draft RFI

Turn officer-approved outstanding matters into a concise, client-ready RFI package while preserving an internal audit trail from each request back to the reviewed assessment.

## Hard Boundaries

- Require a delivered assessment report and the compliance officer's documented review disposition before drafting a client RFI.
- Include only items the officer approved for client follow-up. Do not infer approval from the report's draft recommendation or conditions precedent.
- Never send email, upload documents, contact the client, or mark an RFI as sent.
- Do not expose internal risk ratings, screening rules, investigative hypotheses, privileged commentary, or unnecessary personal data to the client.
- Do not silently broaden, narrow, or resolve an approved request. Record ambiguity as a blocker for the officer.
- Treat the client-facing schedule and internal traceability record as separate artifacts.

## Required Inputs

Identify:

- client-pack path and customer name
- delivered report path and version
- officer name, role, review date, and documented disposition
- approved outstanding register references or explicit approved actions
- response deadline, response channel, sender identity, tone, and entity signature block
- prior RFI versions or client responses, if any

If the officer disposition or approved action scope is missing, stop after identifying the missing authorization. Do not create a client-facing draft.

## Workflow

Read `references/rfi-workflow.md` and follow its gates.

1. Verify the delivered report, officer disposition, and approved action scope.
2. Create or update `actions/action-register.md` from the bundled template.
3. Reconcile approved actions against the report's outstanding information, document, and clarification registers.
4. Draft a versioned email, client-facing request schedule, and internal traceability record under `actions/rfi/`.
5. Run the completeness, disclosure, tone, and traceability checks in `references/rfi-workflow.md`.
6. Record the package as `drafted-for-officer-review`; never record `approved-to-send` or `sent` without separate documentary evidence.

## Bundled Assets

- `assets/action-register-template.md`: post-review action control record.
- `assets/rfi-email-template.md`: client-facing email draft.
- `assets/rfi-request-schedule-template.md`: client-facing request schedule.
- `assets/rfi-traceability-template.md`: internal mapping from each request to reviewed evidence and officer approval.

Copy and adapt the templates into the case workspace. Do not edit the bundled originals.

## Final Response

Report the paths and versions of the email draft, request schedule, traceability record, and action register. Name unresolved officer decisions and confirm explicitly that nothing was sent.
