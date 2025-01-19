import pytest
from src.repositories.mock.get_activity_request_repository import GetActivityRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_activity_service import FitbitActivityService
from src.config import settings

@pytest.fixture
def get_user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def get_user_token_repository(db_session):
    return UserTokenRepository(db_session)

@pytest.fixture
def get_step_request_repository():
    return GetActivityRequestRepository()

def test_get_step(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitActivityService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        activity_request_repository=get_step_request_repository
    )
    step = service.get_steps(1, "2021-01-01")
    assert step == 13327

def test_get_step_intraday(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitActivityService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        activity_request_repository=get_step_request_repository
    )
    steps_intraday = service.get_steps_intraday(1, "2021-01-01", 15)
    expected = [
        {
            "time": "00:00:00",
            "value": 38
        },
        {
            "time": "00:15:00",
            "value": 0
        },
        {
            "time": "00:30:00",
            "value": 0
        },
        {
            "time": "00:45:00",
            "value": 0
        },
        {
            "time": "01:00:00",
            "value": 35
        },
        {
            "time": "01:15:00",
            "value": 30
        },
        {
            "time": "01:30:00",
            "value": 0
        },
        {
            "time": "01:45:00",
            "value": 0
        },
        {
            "time": "02:00:00",
            "value": 0
        },
        {
            "time": "02:15:00",
            "value": 0
        },
        {
            "time": "02:30:00",
            "value": 0
        },
        {
            "time": "02:45:00",
            "value": 0
        },
        {
            "time": "03:00:00",
            "value": 0
        },
        {
            "time": "03:15:00",
            "value": 0
        },
        {
            "time": "03:30:00",
            "value": 0
        },
        {
            "time": "03:45:00",
            "value": 0
        },
        {
            "time": "04:00:00",
            "value": 0
        },
        {
            "time": "04:15:00",
            "value": 0
        },
        {
            "time": "04:30:00",
            "value": 0
        },
        {
            "time": "04:45:00",
            "value": 0
        },
        {
            "time": "05:00:00",
            "value": 0
        },
        {
            "time": "05:15:00",
            "value": 0
        },
        {
            "time": "05:30:00",
            "value": 0
        },
        {
            "time": "05:45:00",
            "value": 29
        },
        {
            "time": "06:00:00",
            "value": 0
        },
        {
            "time": "06:15:00",
            "value": 13
        },
        {
            "time": "06:30:00",
            "value": 1517
        },
        {
            "time": "06:45:00",
            "value": 534
        },
        {
            "time": "07:00:00",
            "value": 0
        },
        {
            "time": "07:15:00",
            "value": 19
        },
        {
            "time": "07:30:00",
            "value": 0
        },
        {
            "time": "07:45:00",
            "value": 26
        },
        {
            "time": "08:00:00",
            "value": 0
        },
        {
            "time": "08:15:00",
            "value": 47
        },
        {
            "time": "08:30:00",
            "value": 6
        },
        {
            "time": "08:45:00",
            "value": 9
        },
        {
            "time": "09:00:00",
            "value": 0
        },
        {
            "time": "09:15:00",
            "value": 0
        },
        {
            "time": "09:30:00",
            "value": 0
        },
        {
            "time": "09:45:00",
            "value": 140
        },
        {
            "time": "10:00:00",
            "value": 0
        },
        {
            "time": "10:15:00",
            "value": 0
        },
        {
            "time": "10:30:00",
            "value": 0
        },
        {
            "time": "10:45:00",
            "value": 0
        },
        {
            "time": "11:00:00",
            "value": 0
        },
        {
            "time": "11:15:00",
            "value": 0
        },
        {
            "time": "11:30:00",
            "value": 78
        },
        {
            "time": "11:45:00",
            "value": 21
        },
        {
            "time": "12:00:00",
            "value": 74
        },
        {
            "time": "12:15:00",
            "value": 24
        },
        {
            "time": "12:30:00",
            "value": 14
        },
        {
            "time": "12:45:00",
            "value": 0
        },
        {
            "time": "13:00:00",
            "value": 28
        },
        {
            "time": "13:15:00",
            "value": 133
        },
        {
            "time": "13:30:00",
            "value": 54
        },
        {
            "time": "13:45:00",
            "value": 38
        },
        {
            "time": "14:00:00",
            "value": 131
        },
        {
            "time": "14:15:00",
            "value": 0
        },
        {
            "time": "14:30:00",
            "value": 0
        },
        {
            "time": "14:45:00",
            "value": 0
        },
        {
            "time": "15:00:00",
            "value": 0
        },
        {
            "time": "15:15:00",
            "value": 0
        },
        {
            "time": "15:30:00",
            "value": 0
        },
        {
            "time": "15:45:00",
            "value": 0
        },
        {
            "time": "16:00:00",
            "value": 146
        },
        {
            "time": "16:15:00",
            "value": 758
        },
        {
            "time": "16:30:00",
            "value": 1422
        },
        {
            "time": "16:45:00",
            "value": 650
        },
        {
            "time": "17:00:00",
            "value": 0
        },
        {
            "time": "17:15:00",
            "value": 32
        },
        {
            "time": "17:30:00",
            "value": 0
        },
        {
            "time": "17:45:00",
            "value": 0
        },
        {
            "time": "18:00:00",
            "value": 0
        },
        {
            "time": "18:15:00",
            "value": 0
        },
        {
            "time": "18:30:00",
            "value": 550
        },
        {
            "time": "18:45:00",
            "value": 1459
        },
        {
            "time": "19:00:00",
            "value": 1365
        },
        {
            "time": "19:15:00",
            "value": 658
        },
        {
            "time": "19:30:00",
            "value": 807
        },
        {
            "time": "19:45:00",
            "value": 1005
        },
        {
            "time": "20:00:00",
            "value": 1402
        },
        {
            "time": "20:15:00",
            "value": 0
        },
        {
            "time": "20:30:00",
            "value": 0
        },
        {
            "time": "20:45:00",
            "value": 0
        },
        {
            "time": "21:00:00",
            "value": 0
        },
        {
            "time": "21:15:00",
            "value": 0
        },
        {
            "time": "21:30:00",
            "value": 0
        },
        {
            "time": "21:45:00",
            "value": 0
        },
        {
            "time": "22:00:00",
            "value": 0
        },
        {
            "time": "22:15:00",
            "value": 0
        },
        {
            "time": "22:30:00",
            "value": 0
        },
        {
            "time": "22:45:00",
            "value": 0
        },
        {
            "time": "23:00:00",
            "value": 0
        },
        {
            "time": "23:15:00",
            "value": 0
        },
        {
            "time": "23:30:00",
            "value": 0
        },
        {
            "time": "23:45:00",
            "value": 0
        }
    ]
    assert steps_intraday == expected