from fastapi import APIRouter, Depends
from src.schemas.fitbit_sleep.fitbit_sleep import FitbitSleepRequest, FitbitSleepResponse, FitbitSleepDetailResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.services.fitbit.fitbit_sleep_service import FitbitSleepService
from src.api.dependencies import get_user_token_repository, get_user_repository
from src.config import settings

router = APIRouter()

@router.get("/fitbit/sleep/{user_id}/{date}", response_model=FitbitSleepResponse)
async def fitbit_sleep(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)
) -> FitbitSleepResponse:
    service = FitbitSleepService(
        setting=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository
    )
    return service.get_sleep_data(user_id, date)

@router.get("/fitbit/sleep/detail/{user_id}/{date}", response_model=FitbitSleepDetailResponse)
async def fitbit_sleep_detail(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)
) -> FitbitSleepDetailResponse:
    service = FitbitSleepService(
        setting=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository
    )
    data = service.get_sleep_detail_data(user_id, date)
    return FitbitSleepDetailResponse(sleep=data)