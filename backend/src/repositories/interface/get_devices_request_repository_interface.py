from abc import ABC, abstractmethod

class GetDevicesRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_devices(self, token: str) -> dict:
        pass