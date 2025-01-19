from fastapi import APIRouter, Depends
from src.schemas.fitbit_activity.fitbit_steps import FitbitActivityResponse,FitbitStepsResponse, FitbitCaloriesIntradayResponse, FitbitStepsIntradayResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_step_request_repository_interface import GetActivityRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_activity_request_repository
from src.services.fitbit.fitbit_activity_service import FitbitActivityService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/activity/{user_id}/{date}", response_model=FitbitActivityResponse)
async def fitbit_activity(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository)
) -> FitbitActivityResponse:
    service = FitbitActivityService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
    )
    activity = service.get_activity(user_id, date)
    
    return FitbitActivityResponse(activity=activity)

@router.get("/fitbit/steps/{user_id}/{date}", response_model=FitbitStepsResponse)
async def fitbit_steps(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository), 
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository)
) -> FitbitStepsResponse:
    service = FitbitActivityService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
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
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository)
) -> FitbitStepsIntradayResponse:
    service = FitbitActivityService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
    )
    steps_intraday = service.get_steps_intraday(user_id, date, detail_level)
    
    return FitbitStepsIntradayResponse(steps_intraday=steps_intraday)

@router.get("/fitbit/calories/intraday/{user_id}/{date}/{detail_level}", response_model=FitbitCaloriesIntradayResponse)
async def fitbit_calories_intraday(
    user_id: int,
    date: str,
    detail_level: int,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository)
) -> FitbitCaloriesIntradayResponse:
    service = FitbitActivityService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
    )
    calories_intraday = service.get_calories_intraday(user_id, date, detail_level)
    
    return FitbitCaloriesIntradayResponse(calories_intraday=calories_intraday)