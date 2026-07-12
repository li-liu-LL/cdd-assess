# CDD Assess

An Agent Skill for turning customer due diligence onboarding materials into source-grounded internal CDD onboarding assessment reports: document review, gap analysis, risk assessment, and a draft recommendation in one document.

It helps Claude Code, Codex, and other Agent Skills-compatible coding agents organize messy client files, build a review bundle, ground the analysis in supplied policies or official sources, and render a versioned HTML report for a qualified compliance officer's review and sign-off.

## What It Covers

- First-run workspace setup and operating-context onboarding
- Client-material inventory, grouping, and source preservation
- Individual and corporate CDD factual records
- Regulatory grounding from supplied policies and primary sources
- SOW, SOF, net worth, expected-activity, and ownership derivations
- Regulatory/licensing assessment and product use-case analysis
- Arithmetic checks, consistency sweeps, citations, and search trails
- Documentary and CDD-form gap analysis with outstanding-matters registers
- Risk assessment (built-in default or entity-supplied methodology), EDD triggers, and a draft onboarding recommendation with conditions precedent
- Explicit phase completion gates, resumable state tracking, and subagent briefs
- Review-bundle templates for consistent output shape
- Mechanical validators for bundle structure, citations, decision-language containment, and render checks
- Print-friendly HTML report assets with A4 pagination

## Installation

```bash
npx skills add li-liu-LL/cdd-assess
```

If your agent runtime does not support the `skills` CLI, copy `skills/cdd-assess` into that runtime's skills directory.

## Usage

Invoke the skill by name:

```text
Use $cdd-assess to organize these onboarding materials and draft a versioned CDD assessment report.
```

The installable skill lives in `skills/cdd-assess/`. Its `SKILL.md` is the entrypoint; supporting references and report assets are loaded only when needed.

`skills/cdd-assess/agents/openai.yaml` is optional UI metadata for agent runtimes that support skill chips, short descriptions, or default prompts. Users do not need to edit it; runtimes that do not use it can ignore it.

## Important Boundary

CDD Assess prepares a complete onboarding assessment, including a draft risk rating and a draft onboarding recommendation. These are proposals only: a qualified compliance officer must review and approve them before any onboarding action, and the officer's documented sign-off is the decision. The report never states that a customer is approved, rejected, or onboarded, and decision language is mechanically confined to the executive summary and the recommendation section.

Do not commit real client materials, rendered reports, or review bundles to this public repository. The `.gitignore` excludes common local testing folders such as `source-drop/`, `client-packs/`, `review-bundle/`, and `reports/`.

## License

MIT
