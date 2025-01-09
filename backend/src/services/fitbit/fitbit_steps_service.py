from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception
from typing import List

class FitbitStepsService:
    def __init__(self, user_token_repository: UserTokenRepositoryInterface):
        """StepsServiceのコンストラクタ
        """
        self.user_token_repository = user_token_repository
    
    def get_steps(self, user_id: int, date: str) -> int:
        """指定した日付の総歩数を取得

        Args:
            user_id (int): ユーザID
            date (str): 日付

        Returns:
            int: 歩数
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        steps = response_json["summary"]["steps"]
        if not steps:
            raise_http_exception(500, "歩数が取得できませんでした")

        return steps
    
    def get_steps_intraday(self, user_id: int, date: str, detail_level: int = 15) -> List:
        """指定した日付のx分ごとの歩数を取得

        Args:
            user_id (int): ユーザID
            date (str): 日付
            detail_level (str): 詳細レベル (1min, 5min, 15min)

        Returns:
            dict: x分ごとの歩数
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        headers = {
            "Authorization": f"Bearer {access_token}"
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
        
        url = f"https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d/{detail_level_str}.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        print(response_json["activities-steps-intraday"])
        steps_intraday = response_json["activities-steps-intraday"]["dataset"]
        return steps_intraday