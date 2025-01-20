from src.config import Settings
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.get_devices_request_repository_interface import GetDevicesRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.string_utility import convert_keys_to_snake_case

class FitbitDevicesService:
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        get_devices_request_repository: GetDevicesRequestRepositoryInterface
    ):
        self.cliend_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.get_devices_request_repository = get_devices_request_repository
    
    def get_devices(self, user_id: int):
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        
        devicesCamel = self.get_devices_request_repository.get_devices(access_token)
        devices = convert_keys_to_snake_case(devicesCamel)
        return devices