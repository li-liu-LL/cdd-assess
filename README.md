# CDD Assess

An Agent Skill for turning customer due diligence onboarding materials into source-grounded internal CDD assessment reports.

It helps Claude Code, Codex, and other Agent Skills-compatible coding agents organize messy client files, build a review bundle, ground the analysis in supplied policies or official sources, and render a versioned HTML report for human compliance review.

## What It Covers

- First-run workspace setup and operating-context onboarding
- Client-material inventory, grouping, and source preservation
- Individual and corporate CDD factual records
- Regulatory grounding from supplied policies and primary sources
- SOW, SOF, net worth, expected-activity, and ownership derivations
- Arithmetic checks, consistency sweeps, citations, and search trails
- Print-friendly HTML report assets with A4 pagination
- A strict boundary against approval, rejection, escalation, or action recommendations

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

CDD Assess prepares review-ready factual material. It does not make regulatory determinations, approve or decline clients, recommend escalation, set conditions, or instruct operational follow-up.

Do not commit real client materials, rendered reports, or review bundles to this public repository. The `.gitignore` excludes common local testing folders such as `source-drop/`, `client-packs/`, `review-bundle/`, and `reports/`.

## License

MIT
