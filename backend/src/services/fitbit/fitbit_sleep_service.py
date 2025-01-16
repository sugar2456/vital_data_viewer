from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.error_response_utility import raise_http_exception
from src.config import Settings
import requests

class FitbitSleepService:
    def __init__(
        self,
        setting: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface
    ):
        self.client_id = setting.fitbit_client_id
        self.client_secret = setting.fitbit_client_secret
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository

    def get_sleep_data(self, user_id: int, date: str):
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
            access_token = fitbit_auth_service.refresh_access_token(
                refresh_token=refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret
            )
        headers = {
            "Authorization": f"Bearer {access_token}"
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

    def get_sleep_detail_data(self, user_id: int, date: str):
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
            access_token = fitbit_auth_service.refresh_access_token(
                refresh_token=refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret
            )
        headers = {
            "Authorization": f"Bearer {access_token}"
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