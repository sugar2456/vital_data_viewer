from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_heart_rate import FitbitHeartRateResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.api.dependencies import get_user_token_repository
from src.services.fitbit.fitbit_heart_rate_service import FitbitHeartRateService

router = APIRouter()

@router.get("/fitbit/heart/{user_id}/{date}", response_model=FitbitHeartRateResponse)
async def fitbit_resting_heart_rate(
    user_id: int,
    date: str,
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)    
) -> FitbitHeartRateResponse:
    service = FitbitHeartRateService(user_token_repository)
    resting_heart_rate = service.get_resting_heart_rate(user_id, date)
    
    return FitbitHeartRateResponse(resting_heart_rate=resting_heart_rate)
