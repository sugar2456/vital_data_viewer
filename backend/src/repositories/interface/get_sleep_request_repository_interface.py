from abc import ABC, abstractmethod

class GetSleepRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_sleep(self, token: str, date: str) -> int:
        pass

    @abstractmethod
    def get_sleep_detail(self, token: str, date: str, detail_level: int):
        pass