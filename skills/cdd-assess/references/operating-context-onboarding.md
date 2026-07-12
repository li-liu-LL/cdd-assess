# Operating Context Onboarding

Use this reference when `OPERATING_CONTEXT.md` is missing, blank, stale, or visibly incomplete. The goal is to make first use feel like guided setup, not interrogation: create useful workspace state immediately, ask one focused question at a time, and let non-critical gaps remain visible as `to confirm`.

## First-Run Behavior

When the folder is empty or no case workspace exists:

1. Create the minimal workspace from `references/workspace-format.md`: `OPERATING_CONTEXT.md`, `MATERIALS.md`, `source-drop/` (with `unassigned/` inside), `knowledge/`, `client-packs/`, and `assets/`.
2. Copy the bundled logo, watermark, template, and CSS into `assets/` if report rendering may happen in this workspace.
3. Write an `OPERATING_CONTEXT.md` draft before asking the first question. Mark unknown values as `to confirm`, not blank.
4. Ask the first blocking question only. Do not present a setup form unless the user asks for one.
5. After each answer, update `OPERATING_CONTEXT.md`, state what can proceed, and ask the next blocking question only if report drafting or material grouping is blocked.

If the folder already contains files, inspect names, paths, obvious policy documents, entity names, and client materials before asking. Facts discoverable from local files belong in the draft with `source: inferred from filename/path/content` and `status: to confirm`. Decisions that affect the review frame still go to the user.

## Intake Priority

Ask in this order, stopping as soon as the next step can proceed:

| Priority | Question | Recommended default | Blocks |
|---|---|---|---|
| 1 | Which regulated entity, jurisdiction, and regulator frame this case? | Use the entity named by the user or the only evident entity file; otherwise ask. | regulatory grounding and report drafting |
| 2 | Where are the client materials? | Use files already in the folder; otherwise ask the user to place or identify the source drop. | grouping and extraction |
| 3 | Is this one client or a mixed source drop? | If filenames show multiple names or IDs, treat as mixed and propose a grouping plan for confirmation. | copying into client packs |
| 4 | Who is the compliance reviewer or preparer for the report metadata? | If unknown, use `to confirm` and continue with analysis, but keep report rendering blocked. | final report rendering |
| 5 | What internal policies, checklists, or knowledge packs apply? | Use supplied files first; if none are provided, proceed with official-source research and record the entity-policy gap. | entity-policy observations |
| 6 | What risk methodology and rating criteria apply? | Ask for the entity's written framework; use the built-in defaults only if the user explicitly instructs, and disclose that in the report. | risk assessment, executive-summary ratings, and recommendation drafting |
| 7 | What source freshness policy and report style requirements apply? | Use conservative defaults: source freshness `to confirm`, audience `internal compliance`, classification `Internal Compliance Use Only`. | final report rendering |

## Blocking Rules

Do not block workspace setup, material inventory, or grouping because context is incomplete.

Block report drafting only when any report-critical field is missing:

- represented entity or jurisdiction/regulator frame
- client material source location
- client grouping confirmation when materials appear mixed
- customer type for the client pack: `individual`, `corporate`, or resolved from `unclear`
- compliance grounding source: supplied policy/knowledge pack or official-source research path

Block final rendering when report metadata remains missing:

- report preparer or reviewer context
- confidentiality/classification text
- logo/watermark choice when the operating context requires branded output

Optional presentation preferences, reviewer names, and policy-pack gaps can stay as `to confirm` if the report clearly marks the limitation and the final self-check records it.

## Question Style

Use concise, decision-oriented questions:

- Ask one question per turn.
- Explain why the question matters in one short clause.
- Include the recommended answer or default.
- Offer a low-friction way to continue, such as "use the files already here" or "mark as to confirm".
- Avoid asking for facts already visible in files.
- Avoid multi-part setup questionnaires unless the user explicitly asks for a form.

Example first question when no facts are visible:

> Which regulated entity and jurisdiction should frame this CDD assessment? Recommended: answer with the entity name plus regulator, for example `Example Securities Ltd / United Kingdom / FCA`; I will mark unknown policy details as `to confirm` and create the workspace now.

Example first question when materials are visible but context is missing:

> I found client materials in `source-drop/`, but no operating context. Should I frame this under `Example Securities Ltd / United Kingdom / FCA`? Recommended: confirm that frame, or give the correct entity/regulator so regulatory grounding uses the right source set.

## OPERATING_CONTEXT.md Shape

Use this shape for the draft and update it after each answer:

```markdown
# Operating Context

Status: draft / ready for analysis / ready for report rendering
Created: YYYY-MM-DD
Last updated: YYYY-MM-DD

## Current Next Step

- Blocking question:
- What can proceed now:
- What remains to confirm:

## Review Frame

| Field | Value | Status | Source / Notes |
|---|---|---|---|
| Represented entity | to confirm | to confirm | |
| Jurisdiction(s) | to confirm | to confirm | |
| Regulator(s) | to confirm | to confirm | |
| Client type(s) handled | to confirm | to confirm | |
| Source freshness policy | to confirm | to confirm | |

## People And Audience

| Field | Value | Status | Source / Notes |
|---|---|---|---|
| Compliance officer / preparer | to confirm | to confirm | |
| Reviewer / team | to confirm | to confirm | |
| Report audience | internal compliance | assumed | default |
| Classification | Internal Compliance Use Only | assumed | default |

## Materials And Policies

| Field | Value | Status | Source / Notes |
|---|---|---|---|
| Source drop path | source-drop/ | assumed | default workspace path |
| Internal policies / checklists | to confirm | to confirm | |
| CDD/onboarding form name and sections | account purpose; product selection; transaction profile; withdrawal limits; SOW/SOF; directors; authorised representatives; authorised platform users; declaration and sign-off | assumed | default section list — replace with the entity's actual form |
| Entity products/services offered | to confirm | to confirm | drives product use-case assessment |
| AML questionnaire policy | to confirm | to confirm | ask; built-in triggers only on explicit instruction |
| Risk methodology | to confirm | to confirm | ask; built-in default only on explicit instruction |
| SOW/SOF rating criteria | to confirm | to confirm | ask; built-in criteria only on explicit instruction |
| Adverse-media web research | disabled | assumed | enable only by explicit user instruction |
| Known gaps | to confirm | to confirm | |

## Report Modules

| Module | Enabled | Precondition | Source / Notes |
|---|---|---|---|
| factual dossier | always | none | core report; cannot be disabled |
| risk assessment and recommendation | always | none | draft for compliance sign-off; see `references/risk-and-recommendation.md` |

## Presentation

| Field | Value | Status | Source / Notes |
|---|---|---|---|
| Logo | assets/logo-placeholder.svg | assumed | replace if supplied |
| Watermark | assets/watermark-placeholder.svg | assumed | replace if supplied |
| Style requirements | default CDD assessment style | assumed | |

## Change Log

| Date | Change | Source |
|---|---|---|
| YYYY-MM-DD | Initial draft created | first-run onboarding |
```

`Status: ready for analysis` means workspace setup, inventory, grouping, extraction, and grounding can proceed. `Status: ready for report rendering` means report-critical metadata and presentation choices are complete enough to render a versioned HTML report.
