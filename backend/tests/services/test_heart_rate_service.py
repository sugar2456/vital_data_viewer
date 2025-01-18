import pytest
from src.repositories.mock.get_heart_rate_repository import GetHeartRateRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_heart_rate_service import FitbitHeartRateService
from src.config import settings

@pytest.fixture
def get_heart_rate_request_repository():
    return GetHeartRateRequestRepository()

@pytest.fixture
def get_user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def get_user_token_repository(db_session):
    return UserTokenRepository(db_session)

def test_get_heart_rate(
    get_user_repository,
    get_user_token_repository,
    get_heart_rate_request_repository
):
    service = FitbitHeartRateService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        get_heart_rate_repository=get_heart_rate_request_repository
    )
    heart_rate = service.get_resting_heart_rate(1, "2021-01-01")
    expexted = {
        "resting_heart_rate": 65
    }
    assert heart_rate == expexted

def test_get_heart_rate_intraday(
    get_user_repository,
    get_user_token_repository,
    get_heart_rate_request_repository
):
    service = FitbitHeartRateService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        get_heart_rate_repository=get_heart_rate_request_repository
    )
    heart_rate_intraday = service.get_heart_rate_intraday(1, "2021-01-01", 1)
    expected = {
        "heart_rate_intraday": [
            {
                "time": "00:00:00",
                "value": 61
            },
            {
                "time": "00:15:00",
                "value": 58
            },
            {
                "time": "00:30:00",
                "value": 58
            },
            {
                "time": "00:45:00",
                "value": 58
            },
            {
                "time": "01:00:00",
                "value": 59
            }
        ]
    }
    assert heart_rate_intraday == expected