from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User

class UsersService:
    """ユーザーサービスクラス
    """
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository
    
    def create_user(self, user_name: str, user_email: str, password: str, fitbit_user_id: str) -> int:
        """ユーザーを作成

        Args:
            user_name (str): ユーザー名
            user_email (str): ユーザーメールアドレス
            password (str): パスワード
            fitbit_user_id (str): fitbitユーザID

        Returns:
            int: 登録したユーザID
        """
        try:
            user = User(
                name=user_name,
                email=user_email,
                hashed_password=password,
                fitbit_user_id=fitbit_user_id
            )
            return self.users_repository.create_user(user).id
        except Exception as e:
            print(f"usersテーブル登録時エラー error: {e}")
            raise e 