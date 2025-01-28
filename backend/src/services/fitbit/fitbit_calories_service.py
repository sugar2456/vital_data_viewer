from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.config import Settings
from typing import List

class FitbitCaloriesService:
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        activity_request_repository: GetActivityRequestRepositoryInterface
    ):
        """StepsServiceのコンストラクタ
        """
        self.settings = settings
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.activity_request_repository = activity_request_repository
        self.cliend_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret

    
    def get_calories_intraday(self, user_id: int, date: str, detail_level: int = 15) -> List:
        """指定した日付のx分ごとの消費カロリーを取得

        Args:
            user_id (int): ユーザID
            date (str): 日付
            detail_level (str): 詳細レベル (1min, 5min, 15min)

        Returns:
            dict: x分ごとの消費カロリー
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_service=None,
                pkce_cache_repository=None,
                user_repository=self.user_repository,
                user_token_repository=self.user_token_repository
            )
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        calories_intraday = self.activity_request_repository.get_activity_intraday(
            token=access_token,
            resource="calories",
            date=date,
            detail_level=detail_level
        )
        return calories_intraday["activities-calories-intraday"]["dataset"]
    
    def get_calories_period(self, user_id: int, start_date: str, end_date: str) -> List:
        """指定した日付の範囲の消費カロリーを取得

        Args:
            user_id (int): ユーザID
            start_date (str): 開始日
            end_date (str): 終了日

        Returns:
            dict: 消費カロリー
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_service=None,
                pkce_cache_repository=None,
                user_repository=self.user_repository,
                user_token_repository=self.user_token_repository
            )
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        calories_range = self.activity_request_repository.get_activity_period(
            token=access_token,
            resource="calories",
            start_date=start_date,
            end_date=end_date
        )
        return calories_range["activities-calories"]

    