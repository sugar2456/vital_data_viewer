from src.repositories.interface.pkce_cache_repostiory_interface import PkceCacheRepositoryInterface
from src.models.pkce_cache import PkceCache
from typing import List
from sqlalchemy.orm import Session

class PkceCacheRepository(PkceCacheRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_pkce_cache(self, state: str) -> PkceCache:
        return self.db.query(PkceCache).filter(PkceCache.state == state).first()

    def create_pkce_cache(self, pkce_cache: PkceCache) -> PkceCache:
        """pkce_cacheを作成する
        

        Args:
            pkce_cache (PkceCache): pkce_cacheのモデル

        Returns:
            PkceCache: 作成されたpkce_cacheのモデル
        """
        add_pkce_cache = PkceCache(
            code_verifier=pkce_cache.code_verifier,
            state=pkce_cache.state
        )
        self.db.add(add_pkce_cache)
        self.db.commit()
        self.db.refresh(add_pkce_cache)
        return add_pkce_cache

    def delete_pkce_cache(self, state: str) -> bool:
        db_pkce_cache = self.get_pkce_cache(state)
        try:
            if db_pkce_cache:
                self.db.delete(db_pkce_cache)
                self.db.commit()
            return True
        except:
            return False