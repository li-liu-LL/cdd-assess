# Workspace Format

Use this structure for each CDD report workspace. In an empty folder, create the minimal skeleton immediately so the user can drop materials into stable locations. For existing folders, create only missing folders needed for the case, but keep names stable once created.

```text
case-workspace/
  OPERATING_CONTEXT.md
  MATERIALS.md
  source-drop/
  compliance-knowledge/
  source-research/
  client-packs/
    001-individual-client-name/
      materials/
      extracted/
      evidence/
      review-bundle/
      specialist-passes/
      reports/
      review-comments/
    002-corporate-client-name/
      materials/
      extracted/
      evidence/
      review-bundle/
      specialist-passes/
      reports/
      review-comments/
  unassigned/
  assets/
```

## Rules

- Keep `source-drop/` untouched after the original materials are copied or linked there.
- Create `OPERATING_CONTEXT.md` from `references/operating-context-onboarding.md`. If incomplete, mark missing fields as `to confirm`; continue workspace setup, inventory, and grouping, but block report drafting while report-critical fields remain unknown.
- Record every received file in `MATERIALS.md`: original path, file name, received date if known, inferred client, status, and notes.
- Confirm the grouping plan before copying files into `client-packs/*/materials/`.
- Name client-pack folders with sequence, customer type, and short customer name: `001-individual-jane-tan`, `002-corporate-acme-pte-ltd`.
- Mark customer type as `individual`, `corporate`, or `unclear`. Resolve `unclear` before drafting that client's report.
- Use `unassigned/` for files that may belong to multiple clients or no identified client.
- Store screenshots, crops, extracted tables, and charts in `evidence/`.
- Store raw specialist outputs in `specialist-passes/` when subagents or separate passes are used.
- Store intermediate outputs in `review-bundle/`; do not rely on the final HTML as the only record.
- Store versioned reports in `reports/` as `v001-individual-jane-tan-onboarding-assessment.html`, `v002-individual-jane-tan-onboarding-assessment.html`, etc.
- Store reviewer notes in `review-comments/`, tied to report version and section.

## Review Bundle

Create these files before rendering HTML:

```text
review-bundle/
  facts.md
  derivations.md
  arithmetic-check.md
  evidence-index.md
  research-summary.md
  completeness-checklist.md
  composition.md
  conflicts-and-gaps.md
  section-outline.md
  review-pass.md
```

Each fact or derivation should include: source, page or section, field name, extraction method, confidence, assumptions if any, and reviewer status. Prefer citation labels like `S1 p.1 section 5 field PEP Declaration`, not bare document labels.

`arithmetic-check.md` should contain the mechanical recomputation record for every number that appears in the report: totals, residuals, ratios, FX conversions, ownership percentages, statement reconciliations, source counts, and key-figure metrics. Save the scratch script or the exact tabular recomputation output here.

`composition.md` should contain the narrative plan: customer story, evidence-strength notes, conflicts, derivation write-ups, observation cards, and print/report-design review notes.

`section-outline.md` should contain the planned report structure and version notes.

If a local runtime permits the older filenames `report-composition.md` or `report-outline.md`, they may be used only as aliases. The portable default names are `composition.md` and `section-outline.md` so common filename guards do not block the workflow.
