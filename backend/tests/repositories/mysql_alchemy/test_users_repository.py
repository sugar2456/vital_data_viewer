import sys
import pytest
from src.repositories.mysql_alchemy.users_repository import UserRepository
from src.models.user import User
from src.constants.users_constants import UsersRoles

@pytest.fixture
def user_repository(db_session):
    return UserRepository(db_session)

def test_create_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_create_user@example.com",
        role=UsersRoles.ADMIN,
        hashed_password="hashed_password",
        fitbit_user_id="X00001"
    )
    created_user = user_repository.create_user(new_user)
    assert created_user.id is not None
    assert created_user.name == "Test User"
    assert created_user.email == "test_create_user@example.com"
    assert created_user.role == UsersRoles.ADMIN

def test_get_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_get_user@example.com",
        role=UsersRoles.USER,
        hashed_password="hashed_password",
        fitbit_user_id="X00002"
    )
    created_user = user_repository.create_user(new_user)
    fetched_user = user_repository.get_user(created_user.id)
    assert fetched_user is not None
    assert fetched_user.id == created_user.id
    assert fetched_user.name == created_user.name
    assert fetched_user.email == created_user.email
    assert fetched_user.role == created_user.role

def test_update_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_update_user@example.com",
        role=UsersRoles.USER,
        hashed_password="hashed_password",
        fitbit_user_id="X00003"
    )
    created_user = user_repository.create_user(new_user)
    created_user.name = "Updated User"
    updated_user = user_repository.update_user(created_user)
    assert updated_user.name == "Updated User"

def test_delete_user(user_repository):
    new_user = User(
        name="Test User",
        email="test_delete_user@example.com",
        role=UsersRoles.USER,
        hashed_password="hashed_password",
        fitbit_user_id="X00004"
    )
    created_user = user_repository.create_user(new_user)
    result = user_repository.delete_user(created_user.id)
    assert result is True
    deleted_user = user_repository.get_user(created_user.id)
    assert deleted_user is None

def test_get_users(user_repository):
    new_user1 = User(
        name="test",
        email="test1@test.com",
        role=UsersRoles.ADMIN,
        hashed_password="test",
        fitbit_user_id="test1"
    )
    new_user2 = User(
        name="test",
        email="test2@test.com",
        role=UsersRoles.USER,
        hashed_password="test",
        fitbit_user_id="test2"
    )
    new_user3 = User(
        name="test",
        email="test3@test.com",
        role=UsersRoles.USER,
        hashed_password="test",
        fitbit_user_id="test3"
    )
    user_repository.create_user(new_user1)
    user_repository.create_user(new_user2)
    user_repository.create_user(new_user3)
    
    users = user_repository.get_users()
    
    assert users[-3].email == new_user1.email
    assert users[-2].email == new_user2.email
    assert users[-1].email == new_user3.email
    assert users[-3].fitbit_user_id == new_user1.fitbit_user_id
    assert users[-2].fitbit_user_id == new_user2.fitbit_user_id
    assert users[-1].fitbit_user_id == new_user3.fitbit_user_id
    assert users[-3].name == new_user1.name
    assert users[-2].name == new_user2.name
    assert users[-1].name == new_user3.name
    assert users[-3].role == new_user1.role
    assert users[-2].role == new_user2.role
    assert users[-1].role == new_user3.role