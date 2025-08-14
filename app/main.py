from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

from .config import settings
from .github_client import github_get, github_post, github_patch


class CreateIssueRequest(BaseModel):
    title: str
    body: Optional[str] = None
    labels: Optional[List[str]] = None
    assignees: Optional[List[str]] = None


class UpdateIssueRequest(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    state: Optional[str] = None
    labels: Optional[List[str]] = None
    assignees: Optional[List[str]] = None


class CreateCommentRequest(BaseModel):
    body: str


app = FastAPI(title='GitHub Connector API', version='0.1.0')


def ensure_allowed(owner: str, repo: str) -> None:
    if not settings.is_allowed(owner, repo):
        raise HTTPException(status_code=403, detail={'code': 'FORBIDDEN', 'message': 'Repository not allowed'})


@app.get('/repos/{owner}/{repo}/issues')
async def list_issues(
    owner: str = Path(...),
    repo: str = Path(...),
    state: Optional[str] = Query(None),
    labels: Optional[str] = Query(None),
    assignee: Optional[str] = Query(None),
    creator: Optional[str] = Query(None),
    since: Optional[str] = Query(None),
    page: Optional[int] = Query(None, ge=1),
    per_page: Optional[int] = Query(None, ge=1, le=100),
):
    ensure_allowed(owner, repo)
    params: Dict[str, Any] = {}
    if state: params['state'] = state
    if labels: params['labels'] = labels
    if assignee: params['assignee'] = assignee
    if creator: params['creator'] = creator
    if since: params['since'] = since
    if page: params['page'] = page
    if per_page: params['per_page'] = per_page

    resp = await github_get(f'/repos/{owner}/{repo}/issues', params=params)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.get('/repos/{owner}/{repo}/issues/{issue_number}')
async def get_issue(
    owner: str = Path(...),
    repo: str = Path(...),
    issue_number: int = Path(...),
):
    ensure_allowed(owner, repo)
    resp = await github_get(f'/repos/{owner}/{repo}/issues/{issue_number}')
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.post('/repos/{owner}/{repo}/issues', status_code=201)
async def create_issue(
    owner: str = Path(...),
    repo: str = Path(...),
    body: CreateIssueRequest = ...,
):
    ensure_allowed(owner, repo)
    payload: Dict[str, Any] = body.dict(exclude_none=True)
    resp = await github_post(f'/repos/{owner}/{repo}/issues', json=payload)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.patch('/repos/{owner}/{repo}/issues/{issue_number}')
async def update_issue(
    owner: str = Path(...),
    repo: str = Path(...),
    issue_number: int = Path(...),
    body: UpdateIssueRequest = ...,
):
    ensure_allowed(owner, repo)
    payload: Dict[str, Any] = body.dict(exclude_none=True)
    resp = await github_patch(f'/repos/{owner}/{repo}/issues/{issue_number}', json=payload)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.get('/repos/{owner}/{repo}/issues/{issue_number}/comments')
async def list_comments(
    owner: str = Path(...),
    repo: str = Path(...),
    issue_number: int = Path(...),
    page: Optional[int] = Query(None, ge=1),
    per_page: Optional[int] = Query(None, ge=1, le=100),
):
    ensure_allowed(owner, repo)
    params: Dict[str, Any] = {}
    if page: params['page'] = page
    if per_page: params['per_page'] = per_page
    resp = await github_get(f'/repos/{owner}/{repo}/issues/{issue_number}/comments', params=params)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.post('/repos/{owner}/{repo}/issues/{issue_number}/comments', status_code=201)
async def add_comment(
    owner: str = Path(...),
    repo: str = Path(...),
    issue_number: int = Path(...),
    body: CreateCommentRequest = ...,
):
    ensure_allowed(owner, repo)
    payload: Dict[str, Any] = body.dict(exclude_none=False)
    resp = await github_post(f'/repos/{owner}/{repo}/issues/{issue_number}/comments', json=payload)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


# Repository contents (read-only)
@app.get('/repos/{owner}/{repo}/contents')
async def list_repo_contents(
    owner: str = Path(...),
    repo: str = Path(...),
    ref: Optional[str] = Query(None, description='Branch/tag/SHA'),
):
    ensure_allowed(owner, repo)
    params: Dict[str, Any] = {}
    if ref:
        params['ref'] = ref
    resp = await github_get(f'/repos/{owner}/{repo}/contents', params=params)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()


@app.get('/repos/{owner}/{repo}/contents/{path:path}')
async def get_repo_content(
    owner: str = Path(...),
    repo: str = Path(...),
    path: str = Path(...),
    ref: Optional[str] = Query(None, description='Branch/tag/SHA'),
):
    ensure_allowed(owner, repo)
    params: Dict[str, Any] = {}
    if ref:
        params['ref'] = ref
    resp = await github_get(f'/repos/{owner}/{repo}/contents/{path}', params=params)
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()
