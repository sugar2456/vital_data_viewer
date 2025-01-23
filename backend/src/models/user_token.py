from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime
from datetime import timedelta, datetime, timezone

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
    
    def __init__(
        self,
        user_id: int,
        access_token: str,
        refresh_token: str,
        token_type: str,
        expires_in: int,
        created_at: datetime = None,
        updated_at: datetime = None
    ):
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
        self.created_at = created_at
        self.updated_at = updated_at
    
    @property
    def is_expired(self) -> bool:
        """アクセストークンが期限切れかどうかを判定

        Returns:
            bool: 期限切れならTrue 期限内ならFalse
        """
        if self.updated_at.tzinfo is None:
            self.updated_at = self.updated_at.replace(tzinfo=timezone.utc)
        expiration_time = self.updated_at + timedelta(seconds=self.expires_in)
        return datetime.now(timezone.utc) > expiration_time