from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User
from typing import List
from sqlalchemy.orm import Session
from src.constants.users_constants import UsersRoles
class UserRepository(UsersRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> User:
        """user_idをもとにusersテーブルからユーザー情報を取得する

        Args:
            user_id (int): ユーザーID

        Returns:
            User: ユーザーモデル
        """
        return User(
            id=user_id,
            name="test",
            email="test1@test.com",
            role=UsersRoles.ADMIN,
            hashed_password="test",
            fitbit_user_id="test"
        )
    
    def get_user_by_fitbit_user_id(self, fitbit_user_id: str) -> User:
        return User(
            id=1,
            name="test",
            email="test1@test.com",
            role=UsersRoles.ADMIN,
            hashed_password="test",
            fitbit_user_id=fitbit_user_id
        )

    def get_users(self) -> List[User]:
        return [
            User(
                id=1,
                name="test",
                email="test1@test.com",
                role=UsersRoles.ADMIN,
                hashed_password="test",
                fitbit_user_id="test1"
            ),
            User(
                id=2,
                name="test",
                email="test2@test.com",
                role=UsersRoles.USER, 
                hashed_password="test",
                fitbit_user_id="test2"
            ),
            User(
                id=3,
                name="test",
                email="test3@test.com",
                role=UsersRoles.ADMIN,
                hashed_password="test",
                fitbit_user_id="test3"
            )
        ]

    def create_user(self, user: User) -> User:
        """userを作成

        Args:
            user (User): 新規で作成するユーザー情報

        Returns:
            User: 登録したユーザー情報
        """
        add_user = User(
            name=user.name,
            email=user.email,
            role=UsersRoles.ADMIN,
            hashed_password=user.hashed_password,
            fitbit_user_id=user.fitbit_user_id,
        )
        add_user.id = 1
        return add_user

    def update_user(self, user: User) -> User:
        return user

    def delete_user(self, user_id: int) -> bool:
        return True