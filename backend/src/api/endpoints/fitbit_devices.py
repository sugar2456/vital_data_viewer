from fastapi import APIRouter, Depends
from src.config import settings
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.api.dependencies import get_user_repository, get_user_token_repository, get_devices_request_repository
from src.schemas.fitbit_devices.fitbit_devices import FitbitDevicesResponse
from src.services.fitbit.fitbit_devices_service import FitbitDevicesService
from src.api.endpoints.auth import get_current_user

router = APIRouter()

@router.get("/fitbit/devices", response_model=FitbitDevicesResponse)
async def fitbit_device(
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    devices_request_repository = Depends(get_devices_request_repository),
    current_user_id: int = Depends(get_current_user)
) -> FitbitDevicesResponse:
    service = FitbitDevicesService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_devices_request_repository=devices_request_repository
    )
    devices = service.get_devices(current_user_id)
    return FitbitDevicesResponse(devices=devices)
    