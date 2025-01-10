from src.utilities.http_utility import HttpUtility
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.utilities.error_response_utility import raise_http_exception
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.config import Settings

class FitbitHeartRateService:
    def __init__(self, settings: Settings, user_token_repository: UserTokenRepositoryInterface):
        """StepsServiceのコンストラクタ
        """
        self.user_token_repository = user_token_repository
        self.cliend_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret

    def get_resting_heart_rate(self, user_id: int, date: str) -> int:
        """指定した日付の安静時の心拍数を取得\n
           完全に安静している時の一分間の心拍数\n
           1日を通して装着している中の一番安定している時の心拍数を取得するので、\n
           睡眠時の心拍数を取得することが多い

        Args:
            user_id (int): ユーザID
            date (str): 日付

        Returns:
            int: 心拍数
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, None, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        url = f"https://api.fitbit.com/1/user/-/activities/heart/date/{date}/1d.json"
        response = HttpUtility.get(url, headers)
        response_json = response.json()
        heart_rate = response_json["activities-heart"][0]["value"]["restingHeartRate"]
        if not heart_rate:
            raise_http_exception(500, "心拍数が取得できませんでした")

        return heart_rate