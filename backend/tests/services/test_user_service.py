import sys
import pytest
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.error_users_repository import ErrorUserRepository
from src.models.user import User
from src.services.users.users_service import UsersService

@pytest.fixture
def user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def error_user_repository(db_session):
    return ErrorUserRepository(db_session)

def test_user_service_create_user(user_repository):
    service = UsersService(user_repository)
    newUser = service.create_user("test", "test1@test.com", 1, "test", "test")
    assert newUser.id is not None
    assert newUser.name == "test"
    assert newUser.email == "test1@test.com"
    assert newUser.role == 1
    assert newUser.fitbit_user_id == "test"
    
def test_user_service_create_user_error(error_user_repository):
    service = UsersService(error_user_repository)
    with pytest.raises(Exception):
        service.create_user("test", "test1@test.com", 2, "test", "test")
