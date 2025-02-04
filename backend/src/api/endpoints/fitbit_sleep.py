from fastapi import APIRouter, Depends
from src.schemas.fitbit_sleep.fitbit_sleep import FitbitSleepRequest, FitbitSleepResponse, FitbitSleepDetailResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_sleep_request_repository_interface import GetSleepRequestRepositoryInterface
from src.services.fitbit.fitbit_sleep_service import FitbitSleepService
from src.api.dependencies import get_user_token_repository, get_user_repository, get_sleep_request_repository
from src.config import settings
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/fitbit/sleep/{date}", response_model=FitbitSleepResponse)
async def fitbit_sleep(
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    get_sleep_request_repository: GetSleepRequestRepositoryInterface = Depends(get_sleep_request_repository),
    current_user_id: str = Depends(get_current_user)
) -> FitbitSleepResponse:
    service = FitbitSleepService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        sleep_request_repository=get_sleep_request_repository
    )
    return service.get_sleep_data(int(current_user_id), date)

@router.get("/fitbit/sleep/detail/{date}", response_model=FitbitSleepDetailResponse)
async def fitbit_sleep_detail(
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    get_sleep_request_repository: GetSleepRequestRepositoryInterface = Depends(get_sleep_request_repository),
    current_user_id: str = Depends(get_current_user)
) -> FitbitSleepDetailResponse:
    service = FitbitSleepService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        sleep_request_repository=get_sleep_request_repository
    )
    data = service.get_sleep_detail_data(int(current_user_id), date)
    return FitbitSleepDetailResponse(sleep=data)