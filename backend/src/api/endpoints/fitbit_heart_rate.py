from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_heart_rate import FitbitHeartRateResponse, FitbitHeartRateIntradayResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.api.dependencies import get_user_token_repository
from src.services.fitbit.fitbit_heart_rate_service import FitbitHeartRateService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/heart/{user_id}/{date}", response_model=FitbitHeartRateResponse)
async def fitbit_resting_heart_rate(
    user_id: int,
    date: str,
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)    
) -> FitbitHeartRateResponse:
    service = FitbitHeartRateService(settings=settings, user_token_repository=user_token_repository)
    resting_heart_rate = service.get_resting_heart_rate(user_id, date)
    
    return FitbitHeartRateResponse(resting_heart_rate=resting_heart_rate)

@router.get("/fitbit/heart/{user_id}/{date}/{detail_level}", response_model=FitbitHeartRateIntradayResponse)
async def fitbit_heart_rate_intraday(
    user_id: int,
    date: str,
    detail_level: int,
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)    
) -> FitbitHeartRateIntradayResponse:
    service = FitbitHeartRateService(settings=settings, user_token_repository=user_token_repository)
    heart_rate_intraday = service.get_heart_rate_intraday(user_id, date, detail_level)
    
    return FitbitHeartRateIntradayResponse(heart_rate_intraday=heart_rate_intraday)