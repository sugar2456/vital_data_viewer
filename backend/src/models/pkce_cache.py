from src.db.session import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

class PkceCache(Base):
    __tablename__ = "pkce_cache"

    id = Column(Integer, primary_key=True, index=True)
    code_verifier = Column(String(255))
    state = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
