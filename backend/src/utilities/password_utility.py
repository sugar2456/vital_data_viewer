from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_temporary_password() -> str:
    return secrets.token_urlsafe(16)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)