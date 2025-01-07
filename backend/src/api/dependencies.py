from sqlalchemy.orm import Session
from src.repositories.mysql_alchemy.pkce_cache_repository import PkceCacheRepository
from src.db.session import get_db
from fastapi import Depends

def get_pkce_cache_repository(db: Session = Depends(get_db)) -> PkceCacheRepository:
    return PkceCacheRepository(db)