from abc import ABC, abstractmethod

class GetBodyRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_body(self, token: str, date: str) -> dict:
        pass
    
    @abstractmethod
    def get_body_period(self, token: str, start_date: str, end_date: str) -> dict:
        pass