from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_steps import FitbitStepsRequest, FitbitStepsResponse, FitbitStepsIntradayRequest, FitbitStepsIntradayResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_step_request_repository_interface import GetStepRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_step_request_repository
from src.services.fitbit.fitbit_steps_service import FitbitStepsService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/steps/{user_id}/{date}", response_model=FitbitStepsResponse)
async def fitbit_steps(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository), 
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    step_request_repository: GetStepRequestRepositoryInterface = Depends(get_step_request_repository)
) -> FitbitStepsResponse:
    service = FitbitStepsService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        step_request_repository=step_request_repository
    )
    steps = service.get_steps(user_id, date)
    
    return FitbitStepsResponse(steps=steps)

@router.get("/fitbit/steps/intraday/{user_id}/{date}/{detail_level}", response_model=FitbitStepsIntradayResponse)
async def fitbit_steps_intraday(
    user_id: int,
    date: str,
    detail_level: int,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    step_request_repository: GetStepRequestRepositoryInterface = Depends(get_step_request_repository)
) -> FitbitStepsIntradayResponse:
    service = FitbitStepsService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        step_request_repository=step_request_repository
    )
    steps_intraday = service.get_steps_intraday(user_id, date, detail_level)
    
    return FitbitStepsIntradayResponse(steps_intraday=steps_intraday)