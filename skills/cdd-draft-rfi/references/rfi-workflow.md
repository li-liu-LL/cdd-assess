# RFI Workflow And Gates

## 1. Verify Authorization

Confirm all of the following from durable case records rather than conversation alone:

- the assessment status is `delivered`
- the report version under review is identified
- the compliance officer's name, role, review date, and disposition are recorded
- each proposed client request has an approved register reference or explicit officer instruction
- any rejected, deferred, internally resolvable, or superseded item is excluded

### Gate — authorized scope ready

Every proposed request is within the officer-approved action scope. Missing or ambiguous scope blocks client-facing drafting.

## 2. Build The Action Register

Copy `assets/action-register-template.md` to `actions/action-register.md`. Use one stable action ID per approved follow-up. Record source report version, register reference, owner, status, due date, and officer authorization evidence.

Do not replace register references with action IDs. Preserve both so later report versions and client responses remain reconcilable.

## 3. Compose Requests

For each approved action:

- request one coherent item or tightly related set of items
- state what is required, the relevant entity/person/time period, and acceptable evidence where approved
- explain the client-facing purpose neutrally without revealing internal risk logic
- distinguish documents, factual information, and clarification questions
- avoid requesting information already present unless the approved action specifically seeks refresh, certification, corroboration, or conflict resolution
- use defined dates rather than relative phrases when a deadline is known
- minimize personal data and avoid asking for credentials, secrets, or insecure transmission

Group requests by topic and order them by what makes response easiest for the client. Preserve stable request IDs across revisions; mark removed items as superseded in the internal records rather than renumbering later items.

## 4. Produce Versioned Artifacts

Create:

```text
actions/
  action-register.md
  rfi/
    v001-email-draft.md
    v001-request-schedule.md
    v001-traceability.md
    review-comments.md
```

Increment the version when approved scope, wording, deadline, recipients, or requested evidence changes. Never overwrite a draft that has already been reviewed.

The client-facing email and schedule contain no internal report/register references unless the officer explicitly wants a neutral case reference shown. The traceability file retains the complete internal mapping.

## 5. Review Checks

Before delivery, confirm:

- every client request maps to exactly one or more approved actions
- every approved action intended for this RFI appears or is recorded as intentionally deferred
- requested items do not duplicate materials already received without an approved reason
- names, legal entities, date ranges, deadlines, and requested formats agree across artifacts
- the email does not imply onboarding approval, rejection, suspicion, or a guaranteed outcome
- no internal risk score, screening configuration, investigative hypothesis, or privileged note is disclosed
- the response channel is approved and appropriate for the information requested
- spelling, tone, numbering, attachments, and signature block are ready for officer review

### Gate — drafted for officer review

All checks pass or each failure is recorded. Set package status to `drafted-for-officer-review` and stop. Sending and external-system submission are outside this skill.
