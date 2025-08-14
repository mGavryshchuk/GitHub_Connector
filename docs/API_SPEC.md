# API Specification (Outline)

The formal specification will live in `openapi.yaml`. Below is the outline.

## Servers
- Local Docker: `http://localhost:8080`

## Security Schemes
- `githubApp` (HTTP bearer): Bearer token is a GitHub App installation token obtained via App JWT exchange
- `pat` (HTTP token): Personal Access Token in `Authorization: token <PAT>`

## Required Headers (proxied)
- `X-Request-ID` (optional): propagated to logs and responses

## Paths (draft)
- GET `/repos/{owner}/{repo}/issues`
  - Query: `state`, `labels`, `assignee`, `creator`, `since`, `page`, `per_page`
  - Security: `githubApp` or `pat`
- GET `/repos/{owner}/{repo}/issues/{issue_number}`
  - Security: `githubApp` or `pat`
- POST `/repos/{owner}/{repo}/issues`
  - Body: `title` (required), `body`, `labels`, `assignees`
  - Security: `githubApp` or `pat`
- PATCH `/repos/{owner}/{repo}/issues/{issue_number}`
  - Body: `title`, `body`, `state`, `labels`, `assignees`
  - Security: `githubApp` or `pat`
- GET `/repos/{owner}/{repo}/issues/{issue_number}/comments`
  - Security: `githubApp` or `pat`
- POST `/repos/{owner}/{repo}/issues/{issue_number}/comments`
  - Body: `body` (required)
  - Security: `githubApp` or `pat`

## Error Model
- Envelope: `{ code: string, message: string, details?: object, requestId?: string }`
- 400: Validation error
- 401/403: Auth/authz error
- 404: Not found
- 409: Conflict
- 429: Rate limited (may include `Retry-After`)
- 5xx: Upstream or internal error

## Notes
- Deleting issues is not supported; closing is used instead.
- Pagination follows GitHub API semantics.
- All requests are validated against OpenAPI schemas; responses normalized.
