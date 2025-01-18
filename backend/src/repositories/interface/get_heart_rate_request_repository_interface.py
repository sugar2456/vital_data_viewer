from abc import ABC, abstractmethod

class GetHeartRateRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_heart_rate(self, token: str, date: str) -> int:
        pass

    @abstractmethod
    def get_heart_rate_intraday(self, token: str, date: str, detail_level: int):
        pass