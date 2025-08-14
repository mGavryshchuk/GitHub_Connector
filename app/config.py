import os
from typing import Set, Optional


def _parse_csv(value: Optional[str]) -> Set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(',') if item.strip()}


class Settings:
    def __init__(self) -> None:
        self.port: int = int(os.getenv('PORT', '8080'))
        self.github_token: Optional[str] = os.getenv('GITHUB_TOKEN')
        self.allowlist_repos: Set[str] = _parse_csv(os.getenv('ALLOWLIST_REPOS'))
        self.allowlist_owners: Set[str] = _parse_csv(os.getenv('ALLOWLIST_OWNERS'))

        if not self.github_token:
            raise RuntimeError('GITHUB_TOKEN is required for PAT authentication')
        if not self.allowlist_repos and not self.allowlist_owners:
            raise RuntimeError('At least one of ALLOWLIST_REPOS or ALLOWLIST_OWNERS must be set')

    def is_allowed(self, owner: str, repo: str) -> bool:
        if f"{owner}/{repo}" in self.allowlist_repos:
            return True
        if owner in self.allowlist_owners:
            return True
        return False


settings = Settings()
