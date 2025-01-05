import sys
import pytest
from src.repositories.mysql_alchemy.users_repository import UserRepository
from src.models.user import User

@pytest.fixture
def user_repository(db_session):
    return UserRepository(db_session)

def test_create_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_create_user@example.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00001",
        fitbit_access_token="fitbit_access_token",
        fitbit_refresh_token="fitbit_refresh_token"
    )
    created_user = user_repository.create_user(new_user)
    assert created_user.id is not None
    assert created_user.name == "Test User"
    assert created_user.email == "test_create_user@example.com"

def test_get_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_get_user@example.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00002",
        fitbit_access_token="fitbit_access_token",
        fitbit_refresh_token="fitbit_refresh_token"
    )
    created_user = user_repository.create_user(new_user)
    fetched_user = user_repository.get_user(created_user.id)
    assert fetched_user is not None
    assert fetched_user.id == created_user.id
    assert fetched_user.name == "Test User"

def test_update_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_update_user@example.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00003",
        fitbit_access_token="fitbit_access_token",
        fitbit_refresh_token="fitbit_refresh_token"
    )
    created_user = user_repository.create_user(new_user)
    created_user.name = "Updated User"
    updated_user = user_repository.update_user(created_user)
    assert updated_user.name == "Updated User"

def test_delete_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_delete_user@example.com",
        hashed_password="hashed_password",
        fitbit_user_id="X00004",
        fitbit_access_token="fitbit_access_token",
        fitbit_refresh_token="fitbit_refresh_token"
    )
    created_user = user_repository.create_user(new_user)
    result = user_repository.delete_user(created_user.id)
    assert result is True
    deleted_user = user_repository.get_user(created_user.id)
    assert deleted_user is None