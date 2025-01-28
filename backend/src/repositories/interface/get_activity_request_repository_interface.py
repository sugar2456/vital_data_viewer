from abc import ABC, abstractmethod

class GetActivityRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_activity(self, token: str, date: str):
        pass

    @abstractmethod
    def get_activity_intraday(self, token: str, resource: str, date: str, detail_level: int):
        pass
    
    @abstractmethod
    def get_activity_period(self, token: str, resource: str, start_date: str, end_date: str):
        pass