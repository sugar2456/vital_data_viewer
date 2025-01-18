from abc import ABC, abstractmethod
from typing import List
from src.models.pkce_cache import PkceCache

class GetStepRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_step(self, token: str, date: str) -> int:
        pass

    @abstractmethod
    def get_step_intraday(self, token: str, date: str, detail_level: int):
        pass