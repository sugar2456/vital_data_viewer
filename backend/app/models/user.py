from sqlalchemy import Column, Integer, String
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    fitbit_user_id = Column(String(255),unique=True, index=True)
    fitbit_access_token = Column(String(255))
    fitbit_refresh_token = Column(String(255))
    