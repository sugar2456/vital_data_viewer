from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.api.dependencies import get_user_repository
from src.services.auth_serivce import AuthService
from src.schemas.auth import Token
from jose import JWTError, jwt
from src.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.secret_algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
) -> Token:
    name = form_data.username
    password = form_data.password
    
    auth_service = AuthService(user_repository)
    token = auth_service.login(name, password)

    return Token(
        access_token=token["access_token"],
        token_type=token["token_type"]
    )