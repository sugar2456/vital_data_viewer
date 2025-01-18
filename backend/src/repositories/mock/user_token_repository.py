from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.models.user_token import UserToken
from sqlalchemy.orm import Session
from datetime import datetime, timezone

class UserTokenRepository(UserTokenRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_token(self, user_id: int) -> UserToken:
        new_user_token = UserToken(
            user_id=1,
            access_token="test",
            refresh_token="test",
            token_type="test",
            expires_in=1,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        return new_user_token
    
    def create_user_token(self, user_token: UserToken) -> UserToken:
        user_token = UserToken(
            user_id=user_token.user_id,
            access_token=user_token.access_token,
            refresh_token=user_token.refresh_token,
            token_type=user_token.token_type,
            expires_in=user_token.expires_in,
        )
        return user_token
    
    def update_user_token(self, user_token: UserToken) -> UserToken:
        db_user_token = self.get_user_token(user_token.user_id)
        db_user_token.access_token = user_token.access_token
        db_user_token.refresh_token = user_token.refresh_token
        db_user_token.token_type = user_token.token_type
        db_user_token.expires_in = user_token.expires_in
        db_user_token.updated_at = datetime.now(timezone.utc)
        return db_user_token
    
    def delete_user_token(self, user_id)-> bool:
        return True