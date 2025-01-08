import pytest
from src.repositories.mysql_alchemy.user_token_repository import UserTokenRepository
from src.repositories.mysql_alchemy.users_repository import UserRepository
from src.models.user_token import UserToken
from src.models.user import User

@pytest.fixture
def user_token_repository(db_session):
    return UserTokenRepository(db_session)

@pytest.fixture
def user_repository(db_session):
    return UserRepository(db_session)

def test_create_user_token(user_token_repository, user_repository):
    new_user = User(
        name="Test User1",
        email="test1@gmail.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00001"
    )
    user_repository.create_user(new_user)
    
    new_user_token = UserToken(
        user_id=1,
        access_token="access_token",
        refresh_token="refresh_token",
        token_type="Bearer",
        expires_in=3600,
    )
    created_user_token = user_token_repository.create_user_token(new_user_token)
    assert created_user_token.id is not None
    assert created_user_token.user_id == 1
    assert created_user_token.access_token == "access_token"
    assert created_user_token.refresh_token == "refresh_token"
    assert created_user_token.token_type == "Bearer"
    assert created_user_token.expires_in == 3600

def test_get_user_token(user_token_repository, user_repository):
    new_user = User(
        name="Test User2",
        email="test2@gmail.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00002"
    )
    user_repository.create_user(new_user)
    new_user_token = UserToken(
        user_id=2,
        access_token="access_token",
        refresh_token="refresh_token",
        token_type="Bearer",
        expires_in=3600,
    )
    user_token_repository.create_user_token(new_user_token)
    retrieved_user_token = user_token_repository.get_user_token(2)
    assert retrieved_user_token is not None
    assert retrieved_user_token.access_token == "access_token"
    assert retrieved_user_token.refresh_token == "refresh_token"
    assert retrieved_user_token.token_type == "Bearer"
    assert retrieved_user_token.expires_in == 3600

def test_update_user_token(user_token_repository, user_repository):
    new_user = User(
        name="Test User3",
        email="test3@gmail.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00003"
    )
    user_repository.create_user(new_user)
    
    new_user_token = UserToken(
        user_id=3,
        access_token="access_token",
        refresh_token="refresh_token",
        token_type="Bearer",
        expires_in=3600,
    )
    created_user_token = user_token_repository.create_user_token(new_user_token)
    
    updated_user_token = UserToken(
        user_id=3,
        access_token="new_access_token",
        refresh_token="new_refresh_token",
        token_type="Bearer",
        expires_in=7200,
    )
    user_token_repository.update_user_token(updated_user_token)
    retrieved_user_token = user_token_repository.get_user_token(3)
    assert retrieved_user_token.access_token == "new_access_token"
    assert retrieved_user_token.refresh_token == "new_refresh_token"
    assert retrieved_user_token.expires_in == 7200
    
def test_delete_user_token(user_token_repository, user_repository):
    new_user = User(
        name="Test User4",
        email="test4@gmail.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00004"
    )
    user_repository.create_user(new_user)
    
    new_user_token = UserToken(
        user_id=4,
        access_token="access_token",
        refresh_token="refresh_token",
        token_type="Bearer",
        expires_in=3600,
    )
    created_user_token = user_token_repository.create_user_token(new_user_token)
    
    isDelte = user_token_repository.delete_user_token(4)
    
    assert isDelte == True