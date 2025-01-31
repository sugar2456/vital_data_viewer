from fastapi import APIRouter, Depends
from src.schemas.users import UsersResponse, User
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_activity_request_repository
from src.services.users.users_service import UsersService
from src.config import settings

router = APIRouter()

@router.get("/users", response_model=UsersResponse)
async def get_users(user_repository: UsersRepositoryInterface = Depends(get_user_repository)) -> UsersResponse:
    service = UsersService(user_repository)
    users = service.get_users()
    return UsersResponse(users=users)