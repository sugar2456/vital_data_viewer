from src.repositories.interface.get_devices_request_repository_interface import GetDevicesRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetDevicesRequestRepository(GetDevicesRequestRepositoryInterface):
    def get_devices(self, token):
        res = [{'battery': 'Empty', 'batteryLevel': 0, 'deviceVersion': 'MobileTrack', 'features': [], 'id': '2430690588', 'lastSyncTime': '2025-01-19T16:35:58.000', 'type': 'TRACKER'}, {'battery': 'High', 'batteryLevel': 100, 'deviceVersion': 'Google Pixel Watch 3', 'features': [], 'id': '2703980549', 'lastSyncTime': '2025-01-20T11:57:12.000', 'type': 'TRACKER'}]
        return res