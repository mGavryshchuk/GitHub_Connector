# Contributing & Working Agreement

This document defines how we collaborate on the GitHub Connector project.

## Workflow & Communication
- Links: Always provide clickable links to files, commits, PRs, and issues.
- Status updates: When moving an issue to a new status (e.g., In Review), append to the issue:
  - What was done (concise bullet list)
  - Commit link(s)
  - List of changed files (with clickable links)
- Assignment: Assign all created issues to the repository owner by default.
- Status flow: New → In Progress → In Review → Done (wait for review feedback before Done).
- Options & decisions: When there are choices, propose 2–3 options with a clear recommendation and a brief “why”.
- Requirements: Do not change requirements without prior approval.
- Terminal commands: Before running any terminal command, include a short explanation in plain text (not inside the command itself). Keep commands short; avoid long chained commands.
- New projects: If we are working on a new project, always ask whether to initialize a new GitHub repository/project before proceeding.

## Technical Defaults
- API: REST bridge, OpenAPI-first.
- Runtime: Python 3.12, FastAPI, Pydantic, httpx.
- Auth: Start with a fine-grained PAT (Issues R/W, Metadata RO). Optionally migrate to a GitHub App later.
- Access scope: Enforce allowlist via `ALLOWLIST_REPOS` and optional `ALLOWLIST_OWNERS`.
- Packaging: Multi-stage Docker (slim), non-root, healthcheck.
- Configuration: Environment variables only.
- Documentation: English in `.md` files (Ukrainian explanations in chat as needed).

## Scope of these rules
- By default, these rules apply to this repository (GitHub Connector) only.
- If you want to apply them globally to future workspaces/interactions, please confirm explicitly and they will be followed across sessions.
