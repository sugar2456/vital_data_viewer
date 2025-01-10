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
    actual_user_id =service.create_user("test", "test1@test.com", "test", "test")
    assert actual_user_id == 1

def test_user_service_create_user_error(error_user_repository):
    service = UsersService(error_user_repository)
    with pytest.raises(Exception):
        service.create_user("test", "test1@test.com", "test", "test")
