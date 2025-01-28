from fastapi import APIRouter, Depends
from src.schemas.fitbit_calories.fitbit_calories import FitbitCaloriesPeriodResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_activity_request_repository
from src.services.fitbit.fitbit_activity_service import FitbitActivityService
from src.services.fitbit.fitbit_calories_service import FitbitCaloriesService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/calories/{user_id}/{start_date}/{end_date}", response_model=FitbitCaloriesPeriodResponse)
async def fitbit_calories_steps_intraday(
    user_id: int,
    start_date: str,
    end_date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository)
) -> FitbitCaloriesPeriodResponse:
    service = FitbitCaloriesService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
    )
    calories_period = service.get_calories_period(user_id, start_date, end_date)
    
    return FitbitCaloriesPeriodResponse(calories_period=calories_period)