from fastapi import APIRouter, Depends
from src.schemas.fitbit_calories.fitbit_calories import FitbitCaloriesPeriodResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.repositories.interface.get_food_request_repository import GetFoodRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_activity_request_repository, get_food_request_repository
from src.services.fitbit.fitbit_activity_service import FitbitActivityService
from src.services.fitbit.fitbit_calories_service import FitbitCaloriesService
from src.services.fitbit.fitbit_food_service import FitbitFoodService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/calories/{user_id}/{start_date}/{end_date}", response_model=FitbitCaloriesPeriodResponse)
async def fitbit_calories_period(
    user_id: int,
    start_date: str,
    end_date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    activity_request_repository: GetActivityRequestRepositoryInterface = Depends(get_activity_request_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository)
) -> FitbitCaloriesPeriodResponse:
    service = FitbitCaloriesService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        activity_request_repository=activity_request_repository
    )
    consumed_calories_period = service.get_calories_period(user_id, start_date, end_date)
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    intaked_calories_period = food_service.get_food_calories_period(user_id, start_date, end_date)
    total_calories_period = food_service.get_total_calories(consumed_calories_period, intaked_calories_period)

    return FitbitCaloriesPeriodResponse(
        consumed_calories_period=consumed_calories_period,
        intaked_calories_period=intaked_calories_period,
        total_calories_period=total_calories_period
    )