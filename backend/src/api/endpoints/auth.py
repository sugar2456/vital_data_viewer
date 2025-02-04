from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.api.dependencies import get_user_repository
from src.services.auth_serivce import AuthService
from src.schemas.auth import Token

router = APIRouter()

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