import pytest
from src.repositories.mysql_alchemy.pkce_cache_repository import PkceCacheRepository
from src.models.pkce_cache import PkceCache

@pytest.fixture
def pkce_cache_repository(db_session):
    return PkceCacheRepository(db_session)

def test_create_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        state="12345"
    )
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    assert created_pkce_cache.id is not None
    assert created_pkce_cache.code_verifier == "asdfghjkl"
    assert created_pkce_cache.state == "12345"
    
def test_get_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        state="23456"
    )
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    fetched_pkce_cache = pkce_cache_repository.get_pkce_cache(created_pkce_cache.state)
    assert fetched_pkce_cache is not None
    assert fetched_pkce_cache.id == created_pkce_cache.id
    assert fetched_pkce_cache.code_verifier == "asdfghjkl"
    assert fetched_pkce_cache.state == "23456"

def test_delete_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        state="34567"
    )
    
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    deleted_pkce_cache = pkce_cache_repository.delete_pkce_cache(created_pkce_cache.state)
    assert deleted_pkce_cache == True
    fetched_pkce_cache = pkce_cache_repository.get_pkce_cache(created_pkce_cache.state)
    assert fetched_pkce_cache is None
