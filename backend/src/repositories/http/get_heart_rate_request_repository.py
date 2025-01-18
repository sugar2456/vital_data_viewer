from src.repositories.interface.get_heart_rate_request_repository_interface import GetHeartRateRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetHeartRateRequestRepository(GetHeartRateRequestRepositoryInterface):
    def get_heart_rate(self, token: str, date: str) -> int:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"https://api.fitbit.com/1/user/-/activities/heart/date/{date}/1d.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        heart_rate = response_json["activities-heart"][0]["value"]["restingHeartRate"]
        if not heart_rate:
            raise_http_exception(500, "心拍数が取得できませんでした")
        
        return heart_rate
    
    def get_heart_rate_intraday(self, token: str, date: str, detail_level: int):
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
            raise_http_exception(500, "心拍数が取得できませんでした")
        url = f"https://api.fitbit.com/1/user/-/activities/heart/date/{date}/1d/{detail_level_str}.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        heart_rate_intraday = response_json["activities-heart-intraday"]["dataset"]
        if not heart_rate_intraday:
            raise_http_exception(500, "心拍数が取得できませんでした")

        return heart_rate_intraday