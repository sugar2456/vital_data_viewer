from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base

class UserToken(Base):
    __tablename__ = "user_tokens"
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token: str = Column(String(255), nullable=False)
    refresh_token: str = Column(String(255), nullable=True)
    token_type: str = Column(String(40), nullable=False)
    expires_in: int = Column(Integer, nullable=False)
    user = relationship("User", back_populates="tokens")
    
    def __init__(self, user_id: int, access_token: str, refresh_token: str, token_type: str, expires_in: int):
        """UserTokenのコンストラクタ

        Args:
            user_id (int): usersテーブルのid
            access_token (str): アクセストークン
            refresh_token (str): リフレッシュトークン
            token_type (str): トークンタイプ
            expires_in (int): アクセストークンの有効期限(秒)
        """
        self.user_id = user_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.expires_in = expires_in