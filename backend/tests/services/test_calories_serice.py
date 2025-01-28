import pytest
from src.repositories.mock.get_activity_request_repository import GetActivityRequestRepository
from src.repositories.mock.users_repository import UserRepository
from src.repositories.mock.user_token_repository import UserTokenRepository
from src.services.fitbit.fitbit_calories_service import FitbitCaloriesService
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

def test_get_calories_intraday(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitCaloriesService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        activity_request_repository=get_step_request_repository
    )
    calories = service.get_calories_intraday(1, "2021-01-01")
    expexted = [
        {
            "level": 1,
            "mets": 242,
            "time": "00:00:00",
            "value": 24.75902
        },
        {
            "level": 0,
            "mets": 182,
            "time": "00:15:00",
            "value": 18.62042
        },
        {
            "level": 0,
            "mets": 177,
            "time": "00:30:00",
            "value": 18.10887
        },
        {
            "level": 0,
            "mets": 162,
            "time": "00:45:00",
            "value": 16.574219999999997
        },
        {
            "level": 1,
            "mets": 270,
            "time": "01:00:00",
            "value": 27.6237
        },
        {
            "level": 0,
            "mets": 203,
            "time": "01:15:00",
            "value": 20.768929999999997
        },
        {
            "level": 0,
            "mets": 157,
            "time": "01:30:00",
            "value": 16.062669999999997
        },
        {
            "level": 0,
            "mets": 166,
            "time": "01:45:00",
            "value": 16.98349
        },
        {
            "level": 0,
            "mets": 150,
            "time": "02:00:00",
            "value": 15.34665
        },
        {
            "level": 0,
            "mets": 169,
            "time": "02:15:00",
            "value": 17.290559000000002
        },
        {
            "level": 0,
            "mets": 151,
            "time": "02:30:00",
            "value": 15.448960999999999
        },
        {
            "level": 0,
            "mets": 150,
            "time": "02:45:00",
            "value": 15.34665
        },
        {
            "level": 0,
            "mets": 151,
            "time": "03:00:00",
            "value": 15.448960999999999
        },
        {
            "level": 0,
            "mets": 166,
            "time": "03:15:00",
            "value": 16.983732
        },
        {
            "level": 0,
            "mets": 164,
            "time": "03:30:00",
            "value": 16.779168
        },
        {
            "level": 0,
            "mets": 150,
            "time": "03:45:00",
            "value": 15.3468
        },
        {
            "level": 0,
            "mets": 167,
            "time": "04:00:00",
            "value": 17.086104000000002
        },
        {
            "level": 0,
            "mets": 151,
            "time": "04:15:00",
            "value": 15.449112000000001
        },
        {
            "level": 0,
            "mets": 150,
            "time": "04:30:00",
            "value": 15.3468
        },
        {
            "level": 0,
            "mets": 150,
            "time": "04:45:00",
            "value": 15.346940000000002
        },
        {
            "level": 0,
            "mets": 150,
            "time": "05:00:00",
            "value": 15.346950000000001
        },
        {
            "level": 0,
            "mets": 150,
            "time": "05:15:00",
            "value": 15.346950000000001
        },
        {
            "level": 0,
            "mets": 186,
            "time": "05:30:00",
            "value": 19.030218
        },
        {
            "level": 0,
            "mets": 200,
            "time": "05:45:00",
            "value": 20.462600000000002
        },
        {
            "level": 0,
            "mets": 178,
            "time": "06:00:00",
            "value": 18.211714
        },
        {
            "level": 0,
            "mets": 207,
            "time": "06:15:00",
            "value": 21.178791
        },
        {
            "level": 2,
            "mets": 860,
            "time": "06:30:00",
            "value": 87.98918
        },
        {
            "level": 1,
            "mets": 545,
            "time": "06:45:00",
            "value": 55.760585000000006
        },
        {
            "level": 0,
            "mets": 176,
            "time": "07:00:00",
            "value": 18.007088000000003
        },
        {
            "level": 1,
            "mets": 277,
            "time": "07:15:00",
            "value": 28.340701000000003
        },
        {
            "level": 0,
            "mets": 175,
            "time": "07:30:00",
            "value": 17.90488
        },
        {
            "level": 0,
            "mets": 223,
            "time": "07:45:00",
            "value": 22.816022
        },
        {
            "level": 0,
            "mets": 174,
            "time": "08:00:00",
            "value": 17.802636
        },
        {
            "level": 0,
            "mets": 183,
            "time": "08:15:00",
            "value": 18.723461999999998
        },
        {
            "level": 0,
            "mets": 222,
            "time": "08:30:00",
            "value": 22.713708
        },
        {
            "level": 0,
            "mets": 198,
            "time": "08:45:00",
            "value": 20.258172
        },
        {
            "level": 0,
            "mets": 175,
            "time": "09:00:00",
            "value": 17.905112
        },
        {
            "level": 0,
            "mets": 210,
            "time": "09:15:00",
            "value": 21.48615
        },
        {
            "level": 0,
            "mets": 170,
            "time": "09:30:00",
            "value": 17.39355
        },
        {
            "level": 1,
            "mets": 341,
            "time": "09:45:00",
            "value": 34.889415
        },
        {
            "level": 1,
            "mets": 238,
            "time": "10:00:00",
            "value": 24.35097
        },
        {
            "level": 0,
            "mets": 179,
            "time": "10:15:00",
            "value": 18.314384999999998
        },
        {
            "level": 0,
            "mets": 173,
            "time": "10:30:00",
            "value": 17.700495
        },
        {
            "level": 0,
            "mets": 179,
            "time": "10:45:00",
            "value": 18.314384999999998
        },
        {
            "level": 0,
            "mets": 184,
            "time": "11:00:00",
            "value": 18.82596
        },
        {
            "level": 0,
            "mets": 183,
            "time": "11:15:00",
            "value": 18.723644999999998
        },
        {
            "level": 1,
            "mets": 262,
            "time": "11:30:00",
            "value": 26.80653
        },
        {
            "level": 1,
            "mets": 239,
            "time": "11:45:00",
            "value": 24.45343
        },
        {
            "level": 1,
            "mets": 328,
            "time": "12:00:00",
            "value": 33.559648
        },
        {
            "level": 1,
            "mets": 262,
            "time": "12:15:00",
            "value": 26.806792
        },
        {
            "level": 1,
            "mets": 292,
            "time": "12:30:00",
            "value": 29.876272000000004
        },
        {
            "level": 1,
            "mets": 428,
            "time": "12:45:00",
            "value": 43.791248
        },
        {
            "level": 1,
            "mets": 413,
            "time": "13:00:00",
            "value": 42.256508000000004
        },
        {
            "level": 1,
            "mets": 410,
            "time": "13:15:00",
            "value": 41.949957
        },
        {
            "level": 1,
            "mets": 378,
            "time": "13:30:00",
            "value": 38.675825999999994
        },
        {
            "level": 1,
            "mets": 254,
            "time": "13:45:00",
            "value": 25.988518
        },
        {
            "level": 1,
            "mets": 439,
            "time": "14:00:00",
            "value": 44.917162999999995
        },
        {
            "level": 0,
            "mets": 151,
            "time": "14:15:00",
            "value": 15.449867
        },
        {
            "level": 0,
            "mets": 150,
            "time": "14:30:00",
            "value": 15.34751
        },
        {
            "level": 0,
            "mets": 150,
            "time": "14:45:00",
            "value": 15.34612
        },
        {
            "level": 0,
            "mets": 171,
            "time": "15:00:00",
            "value": 17.492255
        },
        {
            "level": 0,
            "mets": 212,
            "time": "15:15:00",
            "value": 21.683438
        },
        {
            "level": 0,
            "mets": 175,
            "time": "15:30:00",
            "value": 17.896794
        },
        {
            "level": 0,
            "mets": 183,
            "time": "15:45:00",
            "value": 18.712507
        },
        {
            "level": 1,
            "mets": 264,
            "time": "16:00:00",
            "value": 26.993584
        },
        {
            "level": 1,
            "mets": 503,
            "time": "16:15:00",
            "value": 51.431247
        },
        {
            "level": 2,
            "mets": 854,
            "time": "16:30:00",
            "value": 87.32100799999999
        },
        {
            "level": 1,
            "mets": 579,
            "time": "16:45:00",
            "value": 59.202897
        },
        {
            "level": 0,
            "mets": 168,
            "time": "17:00:00",
            "value": 17.178277
        },
        {
            "level": 0,
            "mets": 184,
            "time": "17:15:00",
            "value": 18.814368
        },
        {
            "level": 0,
            "mets": 176,
            "time": "17:30:00",
            "value": 17.996506999999998
        },
        {
            "level": 0,
            "mets": 156,
            "time": "17:45:00",
            "value": 15.951624
        },
        {
            "level": 0,
            "mets": 156,
            "time": "18:00:00",
            "value": 15.951655
        },
        {
            "level": 0,
            "mets": 159,
            "time": "18:15:00",
            "value": 16.258598
        },
        {
            "level": 1,
            "mets": 458,
            "time": "18:30:00",
            "value": 46.833248
        },
        {
            "level": 2,
            "mets": 812,
            "time": "18:45:00",
            "value": 83.032422
        },
        {
            "level": 2,
            "mets": 828,
            "time": "19:00:00",
            "value": 84.66932
        },
        {
            "level": 1,
            "mets": 571,
            "time": "19:15:00",
            "value": 58.389318
        },
        {
            "level": 2,
            "mets": 642,
            "time": "19:30:00",
            "value": 65.650249
        },
        {
            "level": 2,
            "mets": 633,
            "time": "19:45:00",
            "value": 64.73070799999999
        },
        {
            "level": 2,
            "mets": 897,
            "time": "20:00:00",
            "value": 91.728117
        },
        {
            "level": 0,
            "mets": 173,
            "time": "20:15:00",
            "value": 17.691229
        },
        {
            "level": 0,
            "mets": 185,
            "time": "20:30:00",
            "value": 18.918558
        },
        {
            "level": 0,
            "mets": 157,
            "time": "20:45:00",
            "value": 16.055291
        },
        {
            "level": 0,
            "mets": 150,
            "time": "21:00:00",
            "value": 15.339559999999999
        },
        {
            "level": 0,
            "mets": 151,
            "time": "21:15:00",
            "value": 15.441995
        },
        {
            "level": 0,
            "mets": 151,
            "time": "21:30:00",
            "value": 15.442025000000001
        },
        {
            "level": 0,
            "mets": 169,
            "time": "21:45:00",
            "value": 17.282984
        },
        {
            "level": 0,
            "mets": 150,
            "time": "22:00:00",
            "value": 15.34005
        },
        {
            "level": 0,
            "mets": 165,
            "time": "22:15:00",
            "value": 16.87413
        },
        {
            "level": 0,
            "mets": 150,
            "time": "22:30:00",
            "value": 15.340280000000002
        },
        {
            "level": 0,
            "mets": 151,
            "time": "22:45:00",
            "value": 15.44272
        },
        {
            "level": 0,
            "mets": 182,
            "time": "23:00:00",
            "value": 18.613139999999998
        },
        {
            "level": 0,
            "mets": 164,
            "time": "23:15:00",
            "value": 16.772424
        },
        {
            "level": 0,
            "mets": 166,
            "time": "23:30:00",
            "value": 16.977152
        },
        {
            "level": 0,
            "mets": 150,
            "time": "23:45:00",
            "value": 15.34083
        }
    ]
        
    assert expexted == calories

def test_get_calories_period(
    get_user_repository,
    get_user_token_repository,
    get_step_request_repository
):
    service = FitbitCaloriesService(
        settings=settings,
        user_repository=get_user_repository,
        user_token_repository=get_user_token_repository,
        activity_request_repository=get_step_request_repository
    )
    calories = service.get_calories_period(1, "2024-12-02", "2024-12-31")
    expexted = [
        {
            "dateTime": "2024-12-02",
            "value": "2548"
        },
        {
            "dateTime": "2024-12-03",
            "value": "2269"
        },
        {
            "dateTime": "2024-12-04",
            "value": "2571"
        },
        {
            "dateTime": "2024-12-05",
            "value": "2485"
        },
        {
            "dateTime": "2024-12-06",
            "value": "2368"
        },
        {
            "dateTime": "2024-12-07",
            "value": "2153"
        },
        {
            "dateTime": "2024-12-08",
            "value": "2263"
        },
        {
            "dateTime": "2024-12-09",
            "value": "2732"
        },
        {
            "dateTime": "2024-12-10",
            "value": "2252"
        },
        {
            "dateTime": "2024-12-11",
            "value": "2372"
        },
        {
            "dateTime": "2024-12-12",
            "value": "2590"
        },
        {
            "dateTime": "2024-12-13",
            "value": "2926"
        },
        {
            "dateTime": "2024-12-14",
            "value": "2367"
        },
        {
            "dateTime": "2024-12-15",
            "value": "3217"
        },
        {
            "dateTime": "2024-12-16",
            "value": "2883"
        },
        {
            "dateTime": "2024-12-17",
            "value": "2460"
        },
        {
            "dateTime": "2024-12-18",
            "value": "2597"
        },
        {
            "dateTime": "2024-12-19",
            "value": "2741"
        },
        {
            "dateTime": "2024-12-20",
            "value": "2002"
        },
        {
            "dateTime": "2024-12-21",
            "value": "2479"
        },
        {
            "dateTime": "2024-12-22",
            "value": "2193"
        },
        {
            "dateTime": "2024-12-23",
            "value": "2133"
        },
        {
            "dateTime": "2024-12-24",
            "value": "1969"
        },
        {
            "dateTime": "2024-12-25",
            "value": "2294"
        },
        {
            "dateTime": "2024-12-26",
            "value": "1976"
        },
        {
            "dateTime": "2024-12-27",
            "value": "2134"
        },
        {
            "dateTime": "2024-12-28",
            "value": "1865"
        },
        {
            "dateTime": "2024-12-29",
            "value": "3126"
        },
        {
            "dateTime": "2024-12-30",
            "value": "1927"
        },
        {
            "dateTime": "2024-12-31",
            "value": "3127"
        }
    ]
    assert expexted == calories
