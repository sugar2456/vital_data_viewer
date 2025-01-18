import pytest
from src.repositories.mock.get_step_request_repository import GetStepRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_steps_service import FitbitStepsService
from src.config import settings

@pytest.fixture
def get_user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def get_user_token_repository(db_session):
    return UserTokenRepository(db_session)

@pytest.fixture
def get_step_request_repository():
    return GetStepRequestRepository()

def test_get_step(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitStepsService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        step_request_repository=get_step_request_repository
    )
    step = service.get_steps(1, "2021-01-01")
    assert step == 10000

def test_get_step_intraday(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitStepsService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        step_request_repository=get_step_request_repository
    )
    steps_intraday = service.get_steps_intraday(1, "2021-01-01", 15)
    expected = {
        "steps_intraday" : [
            {
                "time": "00:00:00",
                "value": 10
            },
            {
                "time": "00:15:00",
                "value": 20
            },
            {
                "time": "00:30:00",
                "value": 30
            },
            {
                "time": "00:45:00",
                "value": 40
            },
            {
                "time": "01:00:00",
                "value": 50
            }
        ]
    }
    assert steps_intraday == expected