import pytest
from src.repositories.mock.get_devices_request_repository import GetDevicesRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_devices_service import FitbitDevicesService
from src.config import settings

@pytest.fixture
def get_user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def get_user_token_repository(db_session):
    return UserTokenRepository(db_session)

@pytest.fixture
def get_devices_request_repository():
    return GetDevicesRequestRepository()

def test_get_devices_service(get_user_repository, get_user_token_repository, get_devices_request_repository):
    service = FitbitDevicesService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        get_devices_request_repository=get_devices_request_repository
    )
    devices = service.get_devices(1)
    excepted = [{'battery': 'Empty', 'battery_level': 0, 'device_version': 'MobileTrack', 'features': [], 'id': '2430690588', 'last_sync_time': '2025-01-19T16:35:58.000', 'type': 'TRACKER'}, {'battery': 'High', 'battery_level': 100, 'device_version': 'Google Pixel Watch 3', 'features': [], 'id': '2703980549', 'last_sync_time': '2025-01-20T11:57:12.000', 'type': 'TRACKER'}]
    
    assert devices == excepted