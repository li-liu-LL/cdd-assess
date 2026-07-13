# Workspace Format

Use this structure for each CDD report workspace. In an empty folder, create the minimal skeleton immediately so the user can drop materials into stable locations. For existing folders, create only missing pieces, and keep names stable once created. Do not invent additional top-level files or folders — no report indexes, render logs, or generator scripts at the workspace root; render checks are disposable and version history lives inside each report.

```text
case-workspace/
  OPERATING_CONTEXT.md      # officer, entity, jurisdiction, policies, report modules
  MATERIALS.md              # inventory of received files + grouping plan
  source-drop/              # originals, untouched; unassigned/ inside for unresolved files
  knowledge/
    supplied/               # user-provided policies, checklists, risk methodology
    research/               # persisted findings per references/research-finding-format.md
  client-packs/
    001-individual-jane-tan/
      materials/            # normalized copies from source-drop
      extracted/            # text, tables, page refs; exhibits/ for crops and screenshots
      review-bundle/        # status.md plus exactly the four analytical files below
      reports/              # versioned HTML + review-comments.md
      actions/              # post-review RFI drafts owned by the cdd-draft-rfi skill
  assets/                   # template, css, logo, watermark copied from the skill
```

## Rules

- Keep `source-drop/` untouched after the original materials are copied or linked there. Files that cannot yet be assigned to one client stay in `source-drop/unassigned/`.
- Create `OPERATING_CONTEXT.md` from `references/operating-context-onboarding.md`. If incomplete, mark missing fields as `to confirm`; continue workspace setup, inventory, and grouping, but block report drafting while report-critical fields remain unknown. If the officer directs drafting on working assumptions, the report cover states the context status.
- Record every received file in `MATERIALS.md`: original path, file name, received date if known, inferred client, status, and notes. The grouping plan lives here too; confirm it before copying files into `client-packs/*/materials/`.
- Name client-pack folders with sequence, customer type, and short customer name: `001-individual-jane-tan`, `002-corporate-acme-pte-ltd`. Mark customer type as `individual`, `corporate`, or `unclear`; resolve `unclear` before drafting that client's report.
- Store versioned reports as `reports/v001-individual-jane-tan-onboarding-assessment.html`, `v002-...`, etc. Reviewer notes go in `reports/review-comments.md`, one section per report version.
- Create review-bundle starter files from `templates/record.md`, `templates/analysis.md`, `templates/composition.md`, and `templates/conflicts-and-gaps.md` when available.
- Track workflow state in `review-bundle/status.md` per the Case States section below; create it from `templates/status.md` when available. This status file is operational metadata and does not replace the four analytical bundle files.
- Do not rely on the final HTML as the only record; the review bundle is the durable working record.
- Keep post-review RFI artifacts under `actions/`. They do not alter the delivered report or analytical bundle unless a client response is formally introduced as new evidence and a new report version is created.

## Review Bundle

Four analytical files plus `status.md`; the analytical files are created before rendering HTML:

```text
review-bundle/
  status.md              # workflow state and blockers per the Case States section below
  record.md              # factual record with field-level citations; source register
                         #   (reliability, extraction, freshness); completeness checklist
                         #   with search trails on every absence row
  analysis.md            # derivations (SOW/SOF/net worth/expected activity); ownership and
                         #   control by layer; consistency sweep; arithmetic check (inputs,
                         #   formulae, and outputs of the mechanical recomputation)
  composition.md         # narrative plan: customer story, evidence strength, observation
                         #   cards, section outline, figure plan, critique-pass notes
  conflicts-and-gaps.md  # materiality-ordered worklist plus outstanding information/
                         #   documents/clarification registers per references/report-composition.md
```

If a pass runs as a subagent, append its raw output under a clearly marked heading in the matching bundle file rather than creating new files or folders. Each fact or derivation includes: source, page or section, field name, extraction method, confidence, assumptions if any, and reviewer status. Prefer citation labels like `S1 p.1 §5 field "PEP Declaration"`, never bare document labels.

## Case States

Track each client pack in `review-bundle/status.md` (from `templates/status.md`) so work can be resumed, audited, and delegated across agents without losing place; update it after each phase. States advance in order. A state marked **(gate n)** advances only when that phase completion gate in `SKILL.md` is satisfied; intra-phase states advance on their own criterion:

1. `intake-created` — `OPERATING_CONTEXT.md` has at least a draft
2. `materials-inventoried` — every received file is listed in `MATERIALS.md`
3. `grouping-confirmed` — files assigned to client packs, or ambiguity recorded in `source-drop/unassigned/`
4. `customer-type-confirmed` — **(gate 2)**
5. `grounding-ready` — **(gate 3)**
6. `extraction-complete` — raw extraction preserved with source/page/field/line references and confidence
7. `record-complete` — `record.md` has source register, factual record, and completeness checklists
8. `analysis-complete` — `analysis.md` has derivations, consistency sweep, licensing/product/risk sections, and arithmetic check
9. `composition-ready` — **(gates 4–5)**
10. `html-rendered` — **(gate 6)**
11. `render-check-passed` — render artifacts inspected per gate 7
12. `delivered` — **(gate 7)**; set as the last workspace action immediately before sending the final response (files cannot change after it is sent)

If a gate cannot be satisfied, keep the current state and record the blocker plus the exact evidence or user decision needed.
