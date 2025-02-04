from abc import ABC, abstractmethod
from typing import List
from src.models.user import User

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass
    
    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass
    
    @abstractmethod
    def get_user_by_fitbit_user_id(self, fitbit_user_id: str) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass