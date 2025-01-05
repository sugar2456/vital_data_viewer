import pytest
from src.repositories.mysql_alchemy.pkce_cache_repository import PkceCacheRepository
from src.models.pkce_cache import PkceCache

@pytest.fixture
def pkce_cache_repository(db_session):
    return PkceCacheRepository(db_session)

def test_create_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        email="create_pkce_cache@gmail.com"
    )
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    assert created_pkce_cache.id is not None
    assert created_pkce_cache.code_verifier == "asdfghjkl"
    assert created_pkce_cache.email == "create_pkce_cache@gmail.com"
    
def test_get_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        email="get_pkce_cache@gmail.com"
    )
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    fetched_pkce_cache = pkce_cache_repository.get_pkce_cache(created_pkce_cache.email)
    assert fetched_pkce_cache is not None
    assert fetched_pkce_cache.id == created_pkce_cache.id
    assert fetched_pkce_cache.code_verifier == "asdfghjkl"
    assert fetched_pkce_cache.email == "get_pkce_cache@gmail.com"

def test_delete_pkce_cache(pkce_cache_repository):
    new_pkce_cache = PkceCache(
        code_verifier="asdfghjkl",
        email="delete_pkce_cache@gmail.com"
    )
    
    created_pkce_cache = pkce_cache_repository.create_pkce_cache(new_pkce_cache)
    deleted_pkce_cache = pkce_cache_repository.delete_pkce_cache(created_pkce_cache.email)
    assert deleted_pkce_cache == True
    fetched_pkce_cache = pkce_cache_repository.get_pkce_cache(created_pkce_cache.email)
    assert fetched_pkce_cache is None
