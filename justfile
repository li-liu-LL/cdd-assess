# Project recipes

set shell := ["bash", "-lc"]

default:
    @just --list

# Start Claude Code with skip permissions
claude *args:
    claude --dangerously-skip-permissions {{args}}

# Start Codex in YOLO mode (bypass approvals + sandbox)
codex *args:
    codex --dangerously-bypass-approvals-and-sandbox {{args}}

