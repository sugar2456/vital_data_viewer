from src.repositories.interface.get_body_request_repository_interface import GetBodyRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetBodyRequestRepository(GetBodyRequestRepositoryInterface):
    def get_body(self, token: str, date: str) -> dict:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"https://api.fitbit.com/1/user/-/body/log/weight/date/{date}.json"
        response = HttpUtility.get(url, headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")        
        response_json = response.json()
        # weightは配列で返ってくる
        # 一番最後のデータを取得する
        body = response_json["weight"][-1]
        if not body:
            raise_http_exception(500, "体重データが取得できませんでした")
        return body
        
    
    def get_body_period(self, token: str, start_date: str, end_date: str) -> dict:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"https://api.fitbit.com/1/user/-/body/log/weight/date/{start_date}/{end_date}.json"
        response = HttpUtility.get(url, headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        
        response_json = response.json()
        body_period = response_json["weight"]
        if not body_period:
            raise_http_exception(500, "体重データが取得できませんでした")
        return body_period