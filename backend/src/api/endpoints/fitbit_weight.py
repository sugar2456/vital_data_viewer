from fastapi import APIRouter, Depends
from src.schemas.fitbit_weight.fitbit_weight import FitbitWeightRequest, FitbitWeightResponse, FitbitWeightPeriodRequest, FitbitWeightPeriodResponse
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.get_body_request_repository_interface import GetBodyRequestRepositoryInterface
from src.api.dependencies import get_user_token_repository, get_user_repository, get_weight_request_repository
from src.services.fitbit.fitbit_weight_service import FitbitWeightService
from src.config import settings

router = APIRouter()

@router.get("/fitbit/weight/{user_id}/{date}", response_model=FitbitWeightResponse)
async def fitbit_weight(
    user_id: int,
    date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    body_request_repository: GetBodyRequestRepositoryInterface = Depends(get_weight_request_repository)
) -> FitbitWeightResponse:
    service = FitbitWeightService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_weight_repository=body_request_repository
    )
    weight = service.get_weight(user_id, date)
    return FitbitWeightResponse(
        bmi=weight["bmi"],
        fat=weight["fat"],
        weight=weight["weight"],
        date=weight["date"]
    )

@router.get("/fitbit/weight/{user_id}/{start_date}/{end_date}", response_model=FitbitWeightPeriodResponse)
async def fitbit_weight(
    user_id: int,
    start_date: str,
    end_date: str,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    body_request_repository: GetBodyRequestRepositoryInterface = Depends(get_weight_request_repository)
) -> FitbitWeightPeriodResponse:
    service = FitbitWeightService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_weight_repository=body_request_repository
    )
    weight_list = service.get_weight_period(user_id, start_date, end_date)
    return FitbitWeightPeriodResponse(weight_list=weight_list)