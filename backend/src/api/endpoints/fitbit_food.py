from fastapi import APIRouter, Depends
from src.schemas.fitbit_food.fitbit_food import FitbitFoodResponse, FitbitFoodPeriodResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_food_request_repository import GetFoodRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_food_request_repository
from src.services.fitbit.fitbit_food_service import FitbitFoodService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/foods/{user_id}/{date}", response_model=FitbitFoodResponse)
async def fitbit_food(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository)
) -> FitbitFoodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods = food_service.get_food(user_id=user_id, date=date)
    return FitbitFoodResponse(
        foods=foods['foods']
    )
    

@router.get("/fitbit/foods/{user_id}/{start_date}/{end_date}", response_model=FitbitFoodPeriodResponse)
async def fitbit_food_period(
    user_id: int,
    start_date: str,
    end_date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository)
) -> FitbitFoodPeriodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods_period = food_service.get_food_period(user_id=user_id, start_date=start_date, end_date=end_date)
    return FitbitFoodPeriodResponse(
        foods_period=foods_period
    )

@router.get("/fitbit/foods/{user_id}/{food_id}", response_model=FitbitFoodResponse)
async def fitbit_food_detail(
    user_id: int,
    food_id: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository)
) -> FitbitFoodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods = food_service.get_food_detail(user_id=user_id, food_id=food_id)
    return FitbitFoodResponse(
        foods=foods['foods']
    )