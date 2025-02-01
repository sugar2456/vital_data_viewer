from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.models.user import User
from src.schemas.users import UsersResponse, User as SchemasUser
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
                role=1,
                hashed_password=password,
                fitbit_user_id=fitbit_user_id
            )
            return self.users_repository.create_user(user).id
        except Exception as e:
            print(f"usersテーブル登録時エラー error: {e}")
            raise e
    
    def get_users(self) -> list:
        """ユーザー一覧を取得

        Returns:
            list: ユーザー一覧
        """
        users_data = self.users_repository.get_users()
        users = []
        for user_data in users_data:
            user = SchemasUser(
                id=user_data.id,
                name=user_data.name,
                email=user_data.email,
                created_at=user_data.created_at.isoformat(),
                updated_at=user_data.updated_at.isoformat()
            )
            users.append(user)
        return users