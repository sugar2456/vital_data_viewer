from fastapi import APIRouter, Depends
from src.schemas.fitbit_food.fitbit_food import FitbitFoodResponse, FitbitFoodPeriodResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_food_request_repository import GetFoodRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_food_request_repository
from src.services.fitbit.fitbit_food_service import FitbitFoodService
from src.config import settings
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/fitbit/foods/{date}", response_model=FitbitFoodResponse)
async def fitbit_food(
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository),
    current_user_id: str = Depends(get_current_user)
) -> FitbitFoodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods = food_service.get_food(user_id=int(current_user_id), date=date)
    return FitbitFoodResponse(
        foods=foods['foods']
    )
    

@router.get("/fitbit/foods/{start_date}/{end_date}", response_model=FitbitFoodPeriodResponse)
async def fitbit_food_period(
    start_date: str,
    end_date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository),
    current_user_id: str = Depends(get_current_user)
) -> FitbitFoodPeriodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods_period = food_service.get_food_period(user_id=int(current_user_id), start_date=start_date, end_date=end_date)
    return FitbitFoodPeriodResponse(
        foods_period=foods_period
    )

@router.get("/fitbit/foods/{food_id}", response_model=FitbitFoodResponse)
async def fitbit_food_detail(
    food_id: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    food_request_repository: GetFoodRequestRepositoryInterface = Depends(get_food_request_repository),
    current_user_id: int = Depends(get_current_user)
) -> FitbitFoodResponse:
    
    food_service = FitbitFoodService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_food_request_repository=food_request_repository
    )
    foods = food_service.get_food_detail(user_id=current_user_id, food_id=food_id)
    return FitbitFoodResponse(
        foods=foods['foods']
    )