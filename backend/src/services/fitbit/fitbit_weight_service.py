from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_body_request_repository_interface import GetBodyRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.http_utility import HttpUtility
from src.config import Settings
from src.utilities.error_response_utility import raise_http_exception

class FitbitWeightService():
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        get_weight_repository: GetBodyRequestRepositoryInterface
    ):
        self.cliend_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.get_weight_repository = get_weight_repository
    
    def get_weight(self, user_id: int, date: str) -> dict:
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

        weight = self.get_weight_repository.get_body(token=access_token, date=date)
        return weight
    
    def get_weight_period(self, user_id: int, start_date: str, end_date: str) -> dict:
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

        weight_period = self.get_weight_repository.get_body_period(token=access_token, start_date=start_date, end_date=end_date)
        return weight_period