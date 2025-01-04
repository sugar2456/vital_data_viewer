from src.db.session import Base
from sqlalchemy import Column, Integer, String

class PkceCache(Base):
    __tablename__ = "pkce_cache"

    id = Column(Integer, primary_key=True, index=True)
    code_verifier = Column(String(255))
    email = Column(String(255), index=True)
