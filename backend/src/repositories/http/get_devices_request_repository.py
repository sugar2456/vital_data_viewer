from src.repositories.interface.get_devices_request_repository_interface import GetDevicesRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetDevicesRequestRepository(GetDevicesRequestRepositoryInterface):
    def get_devices(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        url = "https://api.fitbit.com/1/user/-/devices.json"
        
        response = HttpUtility.get(url, headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        
        if not response.json():
            raise_http_exception(500, "デバイス情報が取得できませんでした")

        return response.json()
