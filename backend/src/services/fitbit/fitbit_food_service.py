from src.config import Settings
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.get_food_request_repository import GetFoodRequestRepositoryInterface
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.string_utility import convert_keys_to_snake_case
from typing import List, Dict

class FitbitFoodService:
    def __init__(
        self,
        settings: Settings,
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface,
        get_food_request_repository: GetFoodRequestRepositoryInterface
    ):
        self.cliend_id = settings.fitbit_client_id
        self.client_secret = settings.fitbit_client_secret
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository
        self.get_food_request_repository = get_food_request_repository
    
    def get_food(self, user_id: int, date: str):
        """食品情報を取得

        Args:
            user_id (int): _description_

        Returns:
            _type_: _description_
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        
        food = self.get_food_request_repository.get_food(access_token, date)
        return food
    
    def get_food_period(self, user_id: int, start_date: str, end_date: str):
        """食事情報を取得

        Args:
            user_id (int): _description_

        Returns:
            _type_: _description_
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        
        food_period = self.get_food_request_repository.get_food_period(access_token, start_date, end_date)
        return food_period
    
    def get_food_calories_period(self, user_id: int, start_date: str, end_date: str):
        """食事情報を取得

        Args:
            user_id (int): _description_

        Returns:
            _type_: _description_
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        
        food_period = self.get_food_request_repository.get_food_caloires_period(access_token, start_date, end_date)
        return food_period["foods-log-caloriesIn"]
    
    def get_total_calories(self, consumed_calories_period: List[Dict[str, int]], intaked_calories_period: List[Dict[str, int]]) -> List[Dict[str, int]]:
        total_calories_period = [
            {
                "dateTime": consumed["dateTime"],
                "value": int(intaked["value"]) - int(consumed["value"])
            }
            for consumed, intaked in zip(consumed_calories_period, intaked_calories_period)
        ]
        return total_calories_period
    
    def get_food_detail(self, user_id: int, food_id: str):
        """食事情報を取得

        Args:
            user_id (int): _description_

        Returns:
            _type_: _description_
        """
        user_token = self.user_token_repository.get_user_token(user_id)
        access_token = user_token.access_token
        if user_token.is_expired:
            fitbit_auth_service = FitbitAuthService(None, None, self.user_repository, self.user_token_repository)
            refresh_token = user_token.refresh_token
            access_token = fitbit_auth_service.refresh_access_token(refresh_token=refresh_token, client_id=self.cliend_id, client_secret=self.client_secret)
        
        food = self.get_food_request_repository.get_food_detail(access_token, food_id)
        return food