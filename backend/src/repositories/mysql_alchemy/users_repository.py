from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User
from typing import List
from sqlalchemy.orm import Session

class UserRepository(UsersRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users(self) -> List[User]:
        pass

    def create_user(self, user: User) -> User:
        add_user = User(
            name=user.name,
            email=user.email,
            hashed_password=user.hashed_password,
            fitbit_user_id=user.fitbit_user_id,
            fitbit_access_token=user.fitbit_access_token,
            fitbit_refresh_token=user.fitbit_refresh_token
        )
        self.db.add(add_user)
        self.db.commit()
        self.db.refresh(add_user)
        return add_user

    def update_user(self, user: User) -> User:
        db_user = self.get(user.id)
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> bool:
        db_user = self.get(user_id)
        try:
            if db_user:
                self.db.delete(db_user)
                self.db.commit()
            return True
        except:
            return False