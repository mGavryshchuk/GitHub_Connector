# Roadmap

This roadmap outlines tasks to be tracked in GitHub Issues and the project board.

## Milestone: Foundation
- [ ] Architecture: Design and document system architecture
- [ ] Decide authentication strategy (GitHub App vs PAT) and document
- [ ] Define OpenAPI contract for issues and comments
- [ ] Scaffold API service (language/runtime TBD) following OpenAPI-first
- [ ] Dockerize the service with production-ready image

## Milestone: Core Features
- [ ] Implement list issues endpoint with filtering/pagination
- [ ] Implement get single issue endpoint
- [ ] Implement create issue endpoint
- [ ] Implement update/close issue endpoint
- [ ] Implement list comments endpoint
- [ ] Implement add comment endpoint

## Milestone: Quality & Security
- [ ] Input/output validation from OpenAPI schema
- [ ] Error handling and standardized error responses
- [ ] Request logging, correlation IDs, baseline metrics
- [ ] Rate limiting/backoff for GitHub API
- [ ] Secrets management and configuration docs

## Milestone: Delivery
- [ ] CI: lint/test/build Docker image
- [ ] CD: publish image to registry
- [ ] Usage docs and examples
- [ ] Versioning and release notes
