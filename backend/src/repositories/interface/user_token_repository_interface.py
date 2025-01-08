from abc import ABC, abstractmethod
from typing import List
from src.models.user_token import UserToken

class UserTokenRepositoryInterface(ABC):
    @abstractmethod
    def get_user_token(self, user_id: int) -> UserToken:
        pass

    @abstractmethod
    def create_user_token(self, user_token: UserToken) -> UserToken:
        pass
    
    @abstractmethod
    def update_user_token(self, user_token: UserToken) -> UserToken:
        pass
    
    @abstractmethod
    def delete_user_token(self, user_id: int) -> bool:
        pass