import pytest
from src.repositories.mock.get_sleep_request_repository import GetSleepRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_sleep_service import FitbitSleepService
from src.config import settings

@pytest.fixture
def get_sleep_request_repository():
    return GetSleepRequestRepository()

@pytest.fixture
def get_user_repository(db_session):
    return UserRepository(db_session)

@pytest.fixture
def get_user_token_repository(db_session):
    return UserTokenRepository(db_session)

def test_get_sleep(
    get_user_repository,
    get_user_token_repository,
    get_sleep_request_repository
):
    service = FitbitSleepService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        sleep_request_repository=get_sleep_request_repository
    )
    sleep = service.get_sleep_data(1, "2021-01-01")
    expexted = {
        "stages": {
            "deep": 16,
            "light": 163,
            "rem": 33,
            "wake": 28
        },
        "totalMinutesAsleep": 212,
        "totalSleepRecords": 1,
        "totalTimeInBed": 240
    }
    assert sleep == expexted

def test_get_sleep_detail(
    get_user_repository,
    get_user_token_repository,
    get_sleep_request_repository
):
    service = FitbitSleepService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        sleep_request_repository=get_sleep_request_repository
    )
    sleep_detail_data = service.get_sleep_detail_data(1, "2021-01-01")
    expected = {
        "sleep": [
            {
                "dateOfSleep": "2024-12-02",
                "duration": 14400000,
                "efficiency": 95,
                "endTime": "2024-12-02T05:33:30.000",
                "infoCode": 0,
                "isMainSleep": True,
                "levels": {
                    "data": [
                        {
                            "dateTime": "2024-12-02T01:33:30.000",
                            "level": "wake",
                            "seconds": 390
                        },
                        {
                            "dateTime": "2024-12-02T01:40:00.000",
                            "level": "light",
                            "seconds": 8970
                        },
                    ],
                    "shortData": [
                        {
                            "dateTime": "2024-12-02T01:43:00.000",
                            "level": "wake",
                            "seconds": 180
                        },
                        {
                            "dateTime": "2024-12-02T01:52:00.000",
                            "level": "wake",
                            "seconds": 180
                        },
                    ],
                    "summary": {
                        "deep": {
                            "count": 1,
                            "minutes": 16,
                            "thirtyDayAvgMinutes": 69
                        },
                        "light": {
                            "count": 17,
                            "minutes": 163,
                            "thirtyDayAvgMinutes": 205
                        },
                        "rem": {
                            "count": 5,
                            "minutes": 33,
                            "thirtyDayAvgMinutes": 86
                        },
                        "wake": {
                            "count": 18,
                            "minutes": 28,
                            "thirtyDayAvgMinutes": 55
                        }
                    }
                },
                "logId": 47645244141,
                "minutesAfterWakeup": 0,
                "minutesAsleep": 212,
                "minutesAwake": 28,
                "minutesToFallAsleep": 0,
                "logType": "auto_detected",
                "startTime": "2024-12-02T01:33:30.000",
                "timeInBed": 240,
                "type": "stages"
            }
        ]
    }
    assert sleep_detail_data == expected