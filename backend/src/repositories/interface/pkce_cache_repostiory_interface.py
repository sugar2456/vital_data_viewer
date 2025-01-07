from abc import ABC, abstractmethod
from typing import List
from src.models.pkce_cache import PkceCache

class PkceCacheRepositoryInterface(ABC):
    @abstractmethod
    def get_pkce_cache(self, state: str) -> PkceCache:
        pass

    @abstractmethod
    def create_pkce_cache(self, pkce_cache: PkceCache) -> PkceCache:
        pass

    @abstractmethod
    def delete_pkce_cache(self, state: str) -> bool:
        pass