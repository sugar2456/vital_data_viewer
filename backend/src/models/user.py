from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    fitbit_user_id = Column(String(255),unique=True, index=True)
    fitbit_access_token = Column(String(255))
    fitbit_refresh_token = Column(String(255))
    tokens = relationship("UserToken", back_populates="user")
    
    def __init__(self, name: str, email: str, hashed_password: str, fitbit_user_id: str, fitbit_access_token: str, fitbit_refresh_token: str):
        """Userのコンストラクタ

        Args:
            name (str): ユーザー名
            email (str): メールアドレス
            hashed_password (str): ハッシュ化されたパスワード
            fitbit_user_id (str): FitbitユーザーID
            fitbit_access_token (str): Fitbitアクセストークン
            fitbit_refresh_token (str): Fitbitリフレッシュトークン
        """
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.fitbit_user_id = fitbit_user_id
        self.fitbit_access_token = fitbit_access_token
        self.fitbit_refresh_token = fitbit_refresh_token