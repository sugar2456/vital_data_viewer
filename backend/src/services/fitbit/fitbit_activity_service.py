from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.http_utility import HttpUtility
from src.config import Settings
from src.utilities.error_response_utility import raise_http_exception
from typing import List

class FitbitActivityService:
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
        
    def get_activity(self,  user_id: int, date: str):
        """指定した日付のアクティビティを取得

        Args:
            token (str): アクセストークン
            date (str): 日付
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_repository=None,
                pkce_cache_repository=None,
                user_repository=self.user_repository,
                user_token_repository=self.user_token_repository
            )
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        summary = self.activity_request_repository.get_activity(token=access_token, date=date)["summary"]

        return summary
        
    
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
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_repository=None,
                pkce_cache_repository=None,
                user_repository=self.user_repository,
                user_token_repository=self.user_token_repository
            )
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        activity = self.activity_request_repository.get_activity(token=access_token, date=date)
        return activity["summary"]["steps"]
    
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
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_repository=None,
                pkce_cache_repository=None,
                user_repository=self.user_repository,
                user_token_repository=self.user_token_repository
            )
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)

        steps_intraday = self.activity_request_repository.get_activity_intraday(
            token=access_token,
            resource="steps",
            date=date,
            detail_level=detail_level
        )
        return steps_intraday["activities-steps-intraday"]["dataset"]
    
    def get_step_calories_intraday(self, user_id: int, date: str, detail_level: int = 15) -> dict:
        """指定した日付のx分ごとのアクティビティを取得

        Args:
            user_id (int): ユーザID
            date (str): 日付
            detail_level (str): 詳細レベル (1min, 5min, 15min)

        Returns:
            dict: x分ごとのアクティビティ
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(
                email_repository=None,
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
            detail_level=15
        )
        
        steps_intraday = self.activity_request_repository.get_activity_intraday(
            token=access_token,
            resource="steps",
            date=date,
            detail_level=detail_level
        )
        
        distance_intraday = self.activity_request_repository.get_activity_intraday(
            token=access_token,
            resource="distance",
            date=date,
            detail_level=detail_level
        )
        
        heart_rate_intraday = self.activity_request_repository.get_activity_intraday(
            token=access_token,
            resource="heart",
            date=date,
            detail_level=detail_level
        )
        
        return {
            "calories": calories_intraday["activities-calories-intraday"]["dataset"],
            "steps": steps_intraday["activities-steps-intraday"]["dataset"],
            "distance": distance_intraday["activities-distance-intraday"]["dataset"],
            "heart_rate": heart_rate_intraday["activities-heart-intraday"]["dataset"]
        }