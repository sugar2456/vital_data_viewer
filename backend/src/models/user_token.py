from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime
from datetime import timedelta, datetime

class UserToken(Base):
    __tablename__ = "user_tokens"
    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token: str = Column(String(512), nullable=False)
    refresh_token: str = Column(String(512), nullable=True)
    token_type: str = Column(String(40), nullable=False)
    expires_in: int = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

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
    
    @property
    def is_expired(self) -> bool:
        """アクセストークンが有効かどうかを返す

        Returns:
            bool: アクセストークンが有効ならTrue、そうでないならFalse
        """
        expiration_time = self.updated_at + timedelta(seconds=self.expires_in)
        if expiration_time < datetime.now():
            return True
        return False