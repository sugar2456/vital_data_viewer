from fastapi import APIRouter, Depends
from src.schemas.users import UsersResponse, UserCreatedRequest, UserCreatedResponse, User
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.pkce_cache_repostiory_interface import PkceCacheRepositoryInterface
from repositories.http.email_repository import EmailRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_email_repository, get_pkce_cache_repository
from src.services.users.users_service import UsersService
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.utilities.password_utility import generate_temporary_password, hash_password
from src.config import settings
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/users", response_model=UsersResponse)
async def get_users(
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    current_user_id: int = Depends(get_current_user)
) -> UsersResponse:
    service = UsersService(user_repository)
    users = service.get_users()
    return UsersResponse(users=users)

@router.post("/users/create", response_model=UserCreatedResponse)
async def crete_user(
    request: UserCreatedRequest,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    email_repository: EmailRepositoryInterface = Depends(get_email_repository),
    pkce_cache_repository: PkceCacheRepositoryInterface = Depends(get_pkce_cache_repository),
    current_user_id: int = Depends(get_current_user)
) -> UserCreatedResponse:
    init_password = generate_temporary_password()
    hashed_password = hash_password(init_password)
    service = UsersService(user_repository)
    created = service.create_user(
        user_name=request.name,
        user_email=request.email,
        role=request.role,
        password=hashed_password,
        fitbit_user_id=request.fitbit_user_id
    )
    resUser = User(
        id=created.id,
        name=request.name,
        email=request.email,
        role=request.role,
        fitbit_user_id=request.fitbit_user_id
    )
    fitbit_auth_service = FitbitAuthService(email_repository, pkce_cache_repository, user_token_repository, user_repository)
    await fitbit_auth_service.get_allow_user_resource(settings.fitbit_client_id, request.email, settings.fitbit_redirect_uri, init_password)
    return UserCreatedResponse(
        created=True,
        user=resUser
    )
    