from src.utilities.http_utility import HttpUtility
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_heart_rate_request_repository_interface import GetHeartRateRequestRepositoryInterface
from src.utilities.error_response_utility import raise_http_exception
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.config import Settings
from typing import List

class FitbitHeartRateService:
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        get_heart_rate_repository: GetHeartRateRequestRepositoryInterface
    ):
        """StepsServiceのコンストラクタ
        """
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.get_heart_rate_repository = get_heart_rate_repository
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
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        heart_rate = self.get_heart_rate_repository.get_heart_rate(access_token, date)
        return heart_rate
    
    def get_heart_rate_intraday(self, user_id: int, date: str, detail_level: int = 15) -> List:
        """指定した日付のx分ごとの心拍数を取得

        Args:
            user_id (int): ユーザID
            date (str): 日付
            detail_level (str): 詳細レベル (1min, 5min, 15min)

        Returns:
            dict: x分ごとの心拍数
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            print("refresh")
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        heart_rate_intraday = self.get_heart_rate_repository.get_heart_rate_intraday(access_token, date, detail_level)
        return heart_rate_intraday