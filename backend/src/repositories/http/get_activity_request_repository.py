from src.repositories.interface.get_step_request_repository_interface import GetActivityRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetActivityRequestRepository(GetActivityRequestRepositoryInterface):
    def get_activity(self, token: str, date: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        if not response_json:
            raise_http_exception(500, "アクティビティが取得できませんでした")
        return response_json

    def get_activity_intraday(self, token: str, resource: str, date: str, detail_level: int):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        # detail_levelが1/5/15分の場合
        detail_level_map = {
            1: "1min",
            5: "5min",
            15: "15min"
        }
        detail_level_str = detail_level_map.get(detail_level)
        if not detail_level_str:
            raise_http_exception(500, "歩数が取得できませんでした")
        
        url = f"https://api.fitbit.com/1/user/-/activities/{resource}/date/{date}/1d/{detail_level_str}.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        return response_json