from typing import Any, Dict, Optional
import httpx
from .config import settings


GITHUB_API_BASE_URL = 'https://api.github.com'


def _auth_headers() -> Dict[str, str]:
    # Fine-grained PATs should use Bearer scheme
    return {
        'Authorization': f'Bearer {settings.github_token}',
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'github-connector/0.1',
    }


async def github_get(path: str, params: Optional[Dict[str, Any]] = None) -> httpx.Response:
    async with httpx.AsyncClient(base_url=GITHUB_API_BASE_URL, headers=_auth_headers(), timeout=30.0) as client:
        resp = await client.get(path, params=params)
        return resp


async def github_post(path: str, json: Dict[str, Any]) -> httpx.Response:
    async with httpx.AsyncClient(base_url=GITHUB_API_BASE_URL, headers=_auth_headers(), timeout=30.0) as client:
        resp = await client.post(path, json=json)
        return resp


async def github_patch(path: str, json: Dict[str, Any]) -> httpx.Response:
    async with httpx.AsyncClient(base_url=GITHUB_API_BASE_URL, headers=_auth_headers(), timeout=30.0) as client:
        resp = await client.patch(path, json=json)
        return resp
