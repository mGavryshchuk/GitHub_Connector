# Authentication Guide

This service supports two authentication strategies for accessing the GitHub API.

- Recommended: GitHub App (installation tokens)
- Fallback: Personal Access Token (PAT)

The service automatically chooses the strategy:
- If `GITHUB_APP_ID` is present, it uses the GitHub App flow
- Otherwise, it expects `GITHUB_TOKEN` and uses PAT

## GitHub App (recommended)

Why: Fine-grained permissions, install per repository, auditable, tokens rotate automatically.

### Create the GitHub App
1) Go to Settings → Developer settings → GitHub Apps → New GitHub App
2) Basic info
   - GitHub App name: GitHub Connector Bridge (or your choice)
   - Homepage URL: your repository URL (optional)
   - Webhook: not required for the current scope (leave disabled)
3) Permissions (Repository permissions)
   - Issues: Read and write
   - Metadata: Read-only
4) Where can this GitHub App be installed?
   - Only on this account (default is fine)
5) Save the app, then Generate a private key (PEM). Keep it secure.

### Install the App to repositories
1) On the App page, click Install App
2) Choose the account and select "Only select repositories"
3) Select the repositories this bridge is allowed to access

### Collect IDs and key
- App ID: shown on the App page
- Installation ID: on the Installations page (click your installation → note the numeric ID in the URL)
- Private key: the PEM file you downloaded; encode it to base64 for `.env`

Base64-encode the PEM (single line):
```bash
base64 -b 0 /path/to/private-key.pem > private_key.b64
```

### Environment variables for GitHub App
- `GITHUB_APP_ID`: numeric App ID, e.g., 123456
- `GITHUB_APP_INSTALLATION_ID`: numeric installation ID, e.g., 987654321
- `GITHUB_APP_PRIVATE_KEY_B64`: the base64 string of your PEM

The service will:
1) Create a short-lived App JWT from `GITHUB_APP_ID` + `GITHUB_APP_PRIVATE_KEY_B64`
2) Exchange the JWT for an installation access token using `GITHUB_APP_INSTALLATION_ID`
3) Use `Authorization: Bearer <installation_token>` for all GitHub API calls

## Personal Access Token (PAT) fallback

Why: Quick local bootstrap when a GitHub App isn’t set up yet.

### Fine-grained PAT (preferred)
1) Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token
2) Repository access: Only select repositories (the same repos you want the bridge to access)
3) Permissions:
   - Issues: Read and write
   - Metadata: Read-only
4) Copy the token value

Set env var:
- `GITHUB_TOKEN`: the token string

All calls use `Authorization: token <GITHUB_TOKEN>`.

### Classic PAT (alternative, not recommended for prod)
- Scope: `repo` (grants broad repo access)

## Scope control (allowlist)
To restrict which repos the service can touch:
- `ALLOWLIST_REPOS`: comma-separated `owner/repo` list, e.g. `user/repoA,org/repoB`
- `ALLOWLIST_OWNERS`: optional comma-separated owners, e.g. `user,org`

A request is permitted only if `owner/repo` ∈ `ALLOWLIST_REPOS` or `owner` ∈ `ALLOWLIST_OWNERS`.

## Quick verification
- PAT: list issues for a repo
```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/<owner>/<repo>/issues?per_page=1
```

- App: the service will handle token exchange; once running, you can hit its health/info endpoint (to be added) to confirm App auth is active.
