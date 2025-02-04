import pytest
from utilities.password_utility import generate_temporary_password, hash_password, create_access_token, verify_password
from datetime import timedelta

def test_generate_temporary_password_length():
    password = generate_temporary_password()
    # 生成されたパスワードの長さが予想通りであることを確認
    assert len(password) == 22

def test_generate_temporary_password_uniqueness():
    passwords = {generate_temporary_password() for _ in range(1000)}
    # 生成されたパスワードがすべてユニークであることを確認
    assert len(passwords) == 1000

def test_hash_password():
    password = "testpassword"
    hashed_password = hash_password(password)
    assert hashed_password != password

def test_verify_password():
    password = "testpassword"
    hashed_password = hash_password(password)
    assert verify_password(password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)

def test_create_access_token():
    data = {"sub": "testuser"}
    token1 = create_access_token(data)
    token2 = create_access_token(data, expires_delta=timedelta(minutes=1))
    token3 = create_access_token({"sub": "anotheruser"})
    
    assert token1 is not None
    assert isinstance(token1, str)
    assert len(token1) > 0
    
    assert token1 != token2
    assert token1 != token3
    assert token2 != token3