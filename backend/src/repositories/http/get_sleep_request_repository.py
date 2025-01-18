from src.repositories.interface.get_sleep_request_repository_interface import GetSleepRequestRepositoryInterface
from src.utilities.error_response_utility import raise_http_exception
import requests

class GetSleepRequestRepository(GetSleepRequestRepositoryInterface):
    def get_sleep(self, token: str, date: str) -> int:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{date}.json'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        response_json = response.json()
        summary = response_json['summary']
        if not summary:
            raise_http_exception(500, "睡眠データが取得できませんでした")
        
        return summary
    
    def get_sleep_detail(self, token: str, date: str, detail_level: int):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f'https://api.fitbit.com/1.2/user/-/sleep/date/{date}.json'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        response_json = response.json()
        sleep_list = response_json['sleep']
        if not sleep_list:
            raise_http_exception(500, "睡眠データが取得できませんでした")
        
        return sleep_list