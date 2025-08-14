# Roadmap

This roadmap outlines tasks to be tracked in GitHub Issues and the project board.

Legend
- [x] Done (implemented and verified locally)
- [ ] Todo / Pending
- (In Review) Implemented; awaiting review/feedback on the board

## Milestone: Foundation
- [x] Architecture: Design and document system architecture — see [docs/ARCHITECTURE.md](./ARCHITECTURE.md)
- [x] Decide authentication strategy (GitHub App vs PAT) and document — PAT-first (fine‑grained), App optional later — see [docs/AUTH.md](./AUTH.md)
- [x] Define OpenAPI contract for issues and comments — see [openapi.yaml](../openapi.yaml) and [docs/API_SPEC.md](./API_SPEC.md)
- [x] Scaffold API service (FastAPI, httpx, Pydantic) following OpenAPI-first — see [app/main.py](../app/main.py)
- [x] Dockerize the service with production-ready image — see [Dockerfile](../Dockerfile)

## Milestone: Core Features
- [x] Implement list issues endpoint (GET `/repos/{owner}/{repo}/issues`) — E2E verified
- (In Review) Implement get single issue endpoint (GET `/repos/{owner}/{repo}/issues/{issue_number}`)
- (In Review) Implement create issue endpoint (POST `/repos/{owner}/{repo}/issues`)
- [ ] Implement update/close issue endpoint (PATCH `/repos/{owner}/{repo}/issues/{issue_number}`)
- (In Review) Implement list comments endpoint (GET `/repos/{owner}/{repo}/issues/{issue_number}/comments`)
- (In Review) Implement add comment endpoint (POST `/repos/{owner}/{repo}/issues/{issue_number}/comments`)
- [ ] Implement list repository contents endpoint (GET `/repos/{owner}/{repo}/contents`)
- [ ] Implement get file content endpoint (GET `/repos/{owner}/{repo}/contents/{path}`)

## Milestone: Quality & Security
- [ ] Input/output validation from OpenAPI schema (request/response validation)
- [ ] Error handling and standardized error responses (normalized envelope)
- [ ] Rate limiting/backoff for GitHub API (decorrelated jitter, return 429 with Retry-After)
- [ ] Request logging and correlation IDs (defer minimal logging until needed)
- [x] Secrets management and configuration docs — see [.env.example](../.env.example) and [docs/AUTH.md](./AUTH.md)

## Milestone: Delivery
- [ ] CI: lint/test/build Docker image
- [ ] CD: publish image to registry
- [x] Usage docs and examples — see [README.md](../README.md)
- [ ] Versioning and release notes

## Next up (priority)
1) Standardized error model and response normalization (map upstream errors)
2) Rate limiting and retry/backoff handling
3) Input/output validation driven by `openapi.yaml`
4) Implement update/close issue and E2E tests
5) Repository browsing endpoints: list contents and get file content
6) Minimal request logging with request IDs
