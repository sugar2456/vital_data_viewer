from datetime import timedelta
from src.utilities.error_response_utility import raise_http_exception
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.utilities.password_utility import create_access_token, verify_password

class AuthService:
    def __init__(self, user_repo: UsersRepositoryInterface):
        self.user_repo = user_repo

    def login(self, email: str, password: str):
        user = self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise_http_exception(
                status_code=400,
                message="メールアドレスとパスワードが一致しません",
            )
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
