# GitHub Connector

Problem Statement: Provide access to GitHub Issues to Cursor when private mode is turned on.

Solution: An API bridge, packaged as a Docker container, that exposes a minimal OpenAPI surface for listing, creating, updating, closing issues, and adding comments. The bridge securely proxies requests to the GitHub API.

## Goals
- Enable read/write access to GitHub Issues from Cursor while preserving privacy controls
- Offer a clean OpenAPI contract for CRUD on issues and comments
- Ship a single Docker image that is easy to run locally or deploy

## High-Level Architecture
See `docs/ARCHITECTURE.md` for details.

## Roadmap
See `docs/ROADMAP.md` for the task breakdown managed via GitHub Issues and Project.

## Quickstart (PAT-based)
1) Create a fine-grained PAT with access to your repo(s): Issues (Read & Write), Metadata (Read-only)
2) Copy `.env.example` to `.env` and set:
   - `GITHUB_TOKEN=<your-token>`
   - `ALLOWLIST_REPOS=mGavryshchuk/GitHub_Connector`
3) Run locally:
   - Python: `pip install -r requirements.txt && uvicorn app.main:app --reload --port 8080`
   - Docker: `docker build -t gh-connector:local . && docker run --rm -p 8080:8080 --env-file .env gh-connector:local`
4) Open API docs: `http://localhost:8080/docs`

## License
TBD (e.g., MIT)
