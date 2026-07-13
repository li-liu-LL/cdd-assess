# CDD Skills

A small Agent Skills suite for source-grounded customer due diligence and reviewed client follow-up.

It helps Claude Code, Codex, and other Agent Skills-compatible coding agents work from one durable case record while keeping compliance decisions and external actions under qualified human control.

## Included Skills

- `cdd-assess` — end-to-end context gathering, regulatory grounding, assessment, review bundle, and versioned HTML report production.
- `cdd-draft-rfi` — converts compliance-officer-approved outstanding matters into a versioned client email draft and request schedule with internal traceability. It never sends email.

## Installation

```bash
npx skills add li-liu-LL/cdd-assess
```

If your agent runtime does not support the `skills` CLI, copy the required folders under `skills/` into that runtime's skills directory.

## Usage

Invoke the skill by name:

```text
Use $cdd-assess to organize these onboarding materials and draft a versioned CDD assessment report.
```

After officer review:

```text
Use $cdd-draft-rfi to turn the officer-approved outstanding matters into an RFI draft. Do not send it.
```

Each folder under `skills/` is independently installable. Its `SKILL.md` is the entrypoint; supporting references and assets are loaded only when needed.

Each `agents/openai.yaml` is optional UI metadata for agent runtimes that support skill chips, short descriptions, or default prompts. Users do not need to edit it; runtimes that do not use it can ignore it.

## Important Boundary

The skills prepare analysis and drafts. A qualified compliance officer's documented disposition remains the decision. External communications require separate, exact authorization; installing a skill does not grant that authorization.

Do not commit real client materials, rendered reports, review bundles, action artifacts, or credentials to this public repository. The `.gitignore` excludes common local case folders.

## License

MIT
