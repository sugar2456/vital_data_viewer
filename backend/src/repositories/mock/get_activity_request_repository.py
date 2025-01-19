from src.repositories.interface.get_step_request_repository_interface import GetActivityRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetStepRequestRepository(GetActivityRequestRepositoryInterface):
    def get_activity(self, token: str, date: str):
        summary = {'activities': [{'logId': 3209737751191788720, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 123, 'distance': 1.50267, 'steps': 2003, 'duration': 1187000, 'lastModified': '2024-12-01T21:52:17.999Z', 'startTime': '06:32', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}, {'logId': 1438953266068818256, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 73, 'distance': 0.76893, 'steps': 1136, 'duration': 737000, 'lastModified': '2024-12-02T07:53:07.572Z', 'startTime': '16:40', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}, {'logId': 6226198639546095512, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 446, 'distance': 4.73882, 'steps': 6679, 'duration': 5383000, 'lastModified': '2024-12-02T11:17:05.521Z', 'startTime': '18:46', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}], 'summary': {'caloriesOut': 2549, 'activityCalories': 1229, 'caloriesBMR': 1473, 'activeScore': -1, 'steps': 13327, 'floors': 10, 'elevation': 30.48, 'sedentaryMinutes': 978, 'lightlyActiveMinutes': 177, 'fairlyActiveMinutes': 34, 'veryActiveMinutes': 64, 'distances': [{'activity': 'total', 'distance': 9.635188}, {'activity': 'tracker', 'distance': 9.6243}, {'activity': 'sedentaryActive', 'distance': 0.599075}, {'activity': 'lightlyActive', 'distance': 1.670713}, {'activity': 'moderatelyActive', 'distance': 2.4371}, {'activity': 'veryActive', 'distance': 4.9283}, {'activity': 'loggedActivities', 'distance': 7.010419999999999}, {'activity': 'Walk', 'distance': 1.50267}, {'activity': 'Walk', 'distance': 0.76893}, {'activity': 'Walk', 'distance': 4.73882}], 'marginalCalories': 885, 'restingHeartRate': 64, 'heartRateZones': [{'minutes': 1439, 'caloriesOut': 2532.885447, 'name': 'Out of Range', 'min': 30, 'max': 113}, {'minutes': 1, 'caloriesOut': 7.362792000000001, 'name': 'Fat Burn', 'min': 114, 'max': 138}, {'minutes': 0, 'caloriesOut': 0.0, 'name': 'Cardio', 'min': 139, 'max': 169}, {'minutes': 0, 'caloriesOut': 0.0, 'name': 'Peak', 'min': 170, 'max': 220}]}, 'goals': {'caloriesOut': 2677, 'steps': 10000, 'distance': 8.05, 'floors': 10, 'activeMinutes': 30}}
        return summary

    def get_activity_intraday(self, token: str, resource: str, date: str, detail_level: int):
        step_intraday = {
            "activities-steps": [
                {
                    "dateTime": "2024-12-02",
                    "value": "13327"
                }
            ],
            "activities-steps-intraday": {
                "dataset": [
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
                ],
                "datasetInterval": 15,
                "datasetType": "minute"
            }
        }
        return step_intraday