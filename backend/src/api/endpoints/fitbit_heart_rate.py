from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_heart_rate import FitbitHeartRateResponse, FitbitHeartRateIntradayResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_heart_rate_request_repository_interface import GetHeartRateRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_heart_rate_request_repository
from src.services.fitbit.fitbit_heart_rate_service import FitbitHeartRateService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/heart/{user_id}/{date}", response_model=FitbitHeartRateResponse)
async def fitbit_resting_heart_rate(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    get_heart_rate_repository: GetHeartRateRequestRepositoryInterface = Depends(get_heart_rate_request_repository)
) -> FitbitHeartRateResponse:
    service = FitbitHeartRateService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_heart_rate_repository=get_heart_rate_repository
    )
    resting_heart_rate = service.get_resting_heart_rate(user_id, date)
    
    return FitbitHeartRateResponse(resting_heart_rate=resting_heart_rate)

@router.get("/fitbit/heart/{user_id}/{date}/{detail_level}", response_model=FitbitHeartRateIntradayResponse)
async def fitbit_heart_rate_intraday(
    user_id: int,
    date: str,
    detail_level: int,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    get_heart_rate_request_repository: GetHeartRateRequestRepositoryInterface = Depends(get_heart_rate_request_repository)
) -> FitbitHeartRateIntradayResponse:
    service = FitbitHeartRateService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_heart_rate_repository=get_heart_rate_request_repository
    )
    heart_rate_intraday = service.get_heart_rate_intraday(user_id, date, detail_level)
    
    return FitbitHeartRateIntradayResponse(heart_rate_intraday=heart_rate_intraday)