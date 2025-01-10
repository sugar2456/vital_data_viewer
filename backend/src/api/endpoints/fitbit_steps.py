from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_steps import FitbitStepsRequest, FitbitStepsResponse, FitbitStepsIntradayRequest, FitbitStepsIntradayResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.api.dependencies import get_user_token_repository
from src.services.fitbit.fitbit_steps_service import FitbitStepsService

router = APIRouter()

@router.get("/fitbit/steps/{user_id}/{date}", response_model=FitbitStepsResponse)
async def fitbit_steps(
    user_id: int,
    date: str,
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)    
) -> FitbitStepsResponse:
    service = FitbitStepsService(user_token_repository)
    steps = service.get_steps(user_id, date)
    
    return FitbitStepsResponse(steps=steps)

@router.get("/fitbit/steps/intraday/{user_id}/{date}/{detail_level}", response_model=FitbitStepsIntradayResponse)
async def fitbit_steps_intraday(
    user_id: int,
    date: str,
    detail_level: int,
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)    
) -> FitbitStepsIntradayResponse:
    service = FitbitStepsService(user_token_repository)
    steps_intraday = service.get_steps_intraday(user_id, date, detail_level)
    
    return FitbitStepsIntradayResponse(steps_intraday=steps_intraday)