from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.models.user_token import UserToken
from sqlalchemy.orm import Session
from datetime import datetime, timezone

class UserTokenRepository(UserTokenRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_token(self, user_id: int) -> UserToken:
        return self.db.query(UserToken).filter(UserToken.user_id == user_id).first()
    
    def create_user_token(self, user_token: UserToken) -> UserToken:
        user_token = UserToken(
            user_id=user_token.user_id,
            access_token=user_token.access_token,
            refresh_token=user_token.refresh_token,
            token_type=user_token.token_type,
            expires_in=user_token.expires_in,
        )
        self.db.add(user_token)
        self.db.commit()
        self.db.refresh(user_token)
        return user_token
    
    def update_user_token(self, user_token: UserToken) -> UserToken:
        db_user_token = self.get_user_token(user_token.user_id)
        db_user_token.access_token = user_token.access_token
        db_user_token.refresh_token = user_token.refresh_token
        db_user_token.token_type = user_token.token_type
        db_user_token.expires_in = user_token.expires_in
        db_user_token.updated_at = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(db_user_token)
        return db_user_token
    
    def delete_user_token(self, user_id)-> bool:
        db_user_token = self.get_user_token(user_id)
        try:
            if db_user_token:
                self.db.delete(db_user_token)
                self.db.commit()
            return True
        except:
            return False