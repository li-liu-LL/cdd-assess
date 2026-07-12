# Case State Machine

Track each client pack explicitly so the workflow can be resumed, audited, and delegated across agents without losing place.

## States

A client pack moves through these states in order. Each state belongs to a SKILL.md workflow phase; the last state of a phase advances only when that phase's completion gate is fully satisfied, and intra-phase states advance on the criteria below.

| # | State | SKILL.md phase | Advance to this state when |
|---|---|---|---|
| 1 | `intake-created` | 1. Operating context | Workspace skeleton exists and `OPERATING_CONTEXT.md` has at least a draft. |
| 2 | `materials-inventoried` | 2. Workspace | Every received file is listed in `MATERIALS.md`. |
| 3 | `grouping-confirmed` | 2. Workspace | Files are assigned to client packs, or ambiguity is recorded in `source-drop/unassigned/`. |
| 4 | `customer-type-confirmed` | 2. Workspace (gate) | Customer type is `individual` or `corporate` and the full "workspace ready" gate is satisfied; `unclear` blocks drafting. |
| 5 | `grounding-ready` | 3. Grounding (gate) | The "grounding ready" gate is satisfied. |
| 6 | `extraction-complete` | 4. Specialist passes | Raw extraction pass output is preserved with source/page/field/line references and confidence. |
| 7 | `record-complete` | 4. Specialist passes | `record.md` contains source register, factual record, and completeness checklist. |
| 8 | `analysis-complete` | 4. Specialist passes | `analysis.md` contains derivations, consistency sweep, conflicts, and arithmetic check. |
| 9 | `composition-ready` | 4–5 (gates) | `composition.md` contains narrative plan, observation cards, figure plan, and critique notes; the "specialist passes complete" and "bundle ready" gates are satisfied. |
| 10 | `html-rendered` | 6. Report (gate) | Versioned HTML exists in `reports/` and the "report rendered" gate is satisfied. |
| 11 | `render-check-passed` | 7. Delivery | PDF and screenshot render checks were inspected. |
| 12 | `delivered` | 7. Delivery (gate) | The final response satisfying the "delivered" gate is fully prepared; set this state as the last workspace action immediately before sending it (files cannot be changed after the response is sent). |

## Status File

Create or update `client-packs/*/review-bundle/status.md` after each phase:

```markdown
# Client Pack Status

Current state: intake-created
Last updated: YYYY-MM-DD
Customer type: individual / corporate / unclear
Current blocker: none / describe blocker

## State Log

| Date | From | To | Evidence of completion | Notes |
|---|---|---|---|---|
```

## Transition Rule

Only advance a state when its criteria above are met — and for gate states, only when the mapped completion gate in `SKILL.md` is satisfied. If a gate cannot be satisfied, keep the current state and record the blocker plus the exact evidence or user decision needed.
