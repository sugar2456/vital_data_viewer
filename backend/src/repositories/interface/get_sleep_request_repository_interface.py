from abc import ABC, abstractmethod
from typing import List
from src.models.pkce_cache import PkceCache

class GetSleepRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_sleep(self, token: str, date: str) -> int:
        pass

    @abstractmethod
    def get_sleep_detail(self, token: str, date: str, detail_level: int):
        pass