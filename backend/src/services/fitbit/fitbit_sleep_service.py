from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_sleep_request_repository_interface import GetSleepRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.error_response_utility import raise_http_exception
from src.config import Settings

class FitbitSleepService:
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        sleep_request_repository: GetSleepRequestRepositoryInterface
    ):
        self.client_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.sleep_request_repository = sleep_request_repository

    def get_sleep_data(self, user_id: int, date: str):
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
            access_token = fitbit_auth_service.refresh_access_token(
                refresh_token=refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret
            )
        summary = self.sleep_request_repository.get_sleep(access_token, date)

        return summary

    def get_sleep_detail_data(self, user_id: int, date: str):
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
            access_token = fitbit_auth_service.refresh_access_token(
                refresh_token=refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret
            )

        sleep_detail = 15
        sleep_list = self.sleep_request_repository.get_sleep_detail(access_token, date, sleep_detail)
        return sleep_list