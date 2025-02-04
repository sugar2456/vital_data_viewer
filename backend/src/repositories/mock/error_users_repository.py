from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User
from typing import List
from sqlalchemy.orm import Session

class ErrorUserRepository(UsersRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> User:
        """user_idをもとにusersテーブルからユーザー情報を取得する

        Args:
            user_id (int): ユーザーID

        Returns:
            User: ユーザーモデル
        """
        raise Exception("例外モック")
    
    def get_user_by_fitbit_user_id(self, fitbit_user_id: str) -> User:
        raise Exception("例外モック")
    
    def get_user_by_email(self, email):
        raise Exception("例外モック")

    def get_users(self) -> List[User]:
        raise Exception("例外モック")

    def create_user(self, user: User) -> User:
        raise Exception("例外モック")

    def update_user(self, user: User) -> User:
        raise Exception("例外モック")

    def delete_user(self, user_id: int) -> bool:
        raise Exception("例外モック")