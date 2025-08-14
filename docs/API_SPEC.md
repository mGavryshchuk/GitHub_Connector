# API Specification (Outline)

The formal specification will live in `openapi.yaml`. Below is the outline.

## Servers
- Local Docker: `http://localhost:8080`

## Security Schemes
- `githubApp`: JWT/installation token flow (preferred)
- `pat`: Personal Access Token via `Authorization: token <PAT>`

## Paths (draft)
- GET `/repos/{owner}/{repo}/issues`
  - Query: `state`, `labels`, `assignee`, `creator`, `since`, `page`, `per_page`
- GET `/repos/{owner}/{repo}/issues/{issue_number}`
- POST `/repos/{owner}/{repo}/issues`
  - Body: `title` (required), `body`, `labels`, `assignees`
- PATCH `/repos/{owner}/{repo}/issues/{issue_number}`
  - Body: `title`, `body`, `state`, `labels`, `assignees`
- GET `/repos/{owner}/{repo}/issues/{issue_number}/comments`
- POST `/repos/{owner}/{repo}/issues/{issue_number}/comments`
  - Body: `body` (required)

## Error Model
- Standardized error envelope with `code`, `message`, `details`.

## Notes
- Deleting issues is not supported; closing is used instead.
- Pagination follows GitHub API semantics.
