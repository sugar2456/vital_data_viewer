from fastapi import APIRouter, Depends
from src.config import settings
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.api.dependencies import get_user_repository, get_user_token_repository, get_devices_request_repository
from src.schemas.fitbit_devices.fitbit_devices import FitbitDevicesResponse
from src.services.fitbit.fitbit_devices_service import FitbitDevicesService
from src.utilities.string_utility import convert_keys_to_snake_case

router = APIRouter()

@router.get("/fitbit/devices/{user_id}", response_model=FitbitDevicesResponse)
async def fitbit_device(
    user_id: int,
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository),
    devices_request_repository = Depends(get_devices_request_repository)
) -> FitbitDevicesResponse:
    service = FitbitDevicesService(
        settings=settings,
        user_repository=user_repository,
        user_token_repository=user_token_repository,
        get_devices_request_repository=devices_request_repository
    )
    devicesCamel = service.get_devices(user_id)
    devices = convert_keys_to_snake_case(devicesCamel)
    return FitbitDevicesResponse(devices=devices)
    