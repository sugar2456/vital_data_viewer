from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User
from typing import List
from sqlalchemy.orm import Session

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
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_fitbit_user_id(self, fitbit_user_id: str) -> User:
        return self.db.query(User).filter(User.fitbit_user_id == fitbit_user_id).first()

    def get_users(self) -> List[User]:
        pass

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
            hashed_password=user.hashed_password,
            fitbit_user_id=user.fitbit_user_id,
        )
        self.db.add(add_user)
        self.db.commit()
        self.db.refresh(add_user)
        return add_user

    def update_user(self, user: User) -> User:
        db_user = self.get_user(user.id)
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            db_user.hashed_password = user.hashed_password
            db_user.fitbit_user_id = user.fitbit_user_id
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> bool:
        db_user = self.get_user(user_id)
        try:
            if db_user:
                self.db.delete(db_user)
                self.db.commit()
            return True
        except:
            return False