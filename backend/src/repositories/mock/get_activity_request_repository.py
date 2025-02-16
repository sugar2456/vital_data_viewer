from repositories.interface.get_activity_request_repository_interface import GetActivityRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception
from src.utilities.file_utility import FileUtility

class GetActivityRequestRepository(GetActivityRequestRepositoryInterface):
    def get_activity(self, token: str, date: str):
        summary = {'activities': [{'logId': 3209737751191788720, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 123, 'distance': 1.50267, 'steps': 2003, 'duration': 1187000, 'lastModified': '2024-12-01T21:52:17.999Z', 'startTime': '06:32', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}, {'logId': 1438953266068818256, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 73, 'distance': 0.76893, 'steps': 1136, 'duration': 737000, 'lastModified': '2024-12-02T07:53:07.572Z', 'startTime': '16:40', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}, {'logId': 6226198639546095512, 'activityId': 90013, 'activityParentId': 90013, 'activityParentName': 'Walk', 'name': 'Walk', 'description': 'Walking less than 2 mph, strolling very slowly', 'calories': 446, 'distance': 4.73882, 'steps': 6679, 'duration': 5383000, 'lastModified': '2024-12-02T11:17:05.521Z', 'startTime': '18:46', 'isFavorite': False, 'hasActiveZoneMinutes': True, 'startDate': '2024-12-02', 'hasStartTime': True}], 'summary': {'caloriesOut': 2549, 'activityCalories': 1229, 'caloriesBMR': 1473, 'activeScore': -1, 'steps': 13327, 'floors': 10, 'elevation': 30.48, 'sedentaryMinutes': 978, 'lightlyActiveMinutes': 177, 'fairlyActiveMinutes': 34, 'veryActiveMinutes': 64, 'distances': [{'activity': 'total', 'distance': 9.635188}, {'activity': 'tracker', 'distance': 9.6243}, {'activity': 'sedentaryActive', 'distance': 0.599075}, {'activity': 'lightlyActive', 'distance': 1.670713}, {'activity': 'moderatelyActive', 'distance': 2.4371}, {'activity': 'veryActive', 'distance': 4.9283}, {'activity': 'loggedActivities', 'distance': 7.010419999999999}, {'activity': 'Walk', 'distance': 1.50267}, {'activity': 'Walk', 'distance': 0.76893}, {'activity': 'Walk', 'distance': 4.73882}], 'marginalCalories': 885, 'restingHeartRate': 64, 'heartRateZones': [{'minutes': 1439, 'caloriesOut': 2532.885447, 'name': 'Out of Range', 'min': 30, 'max': 113}, {'minutes': 1, 'caloriesOut': 7.362792000000001, 'name': 'Fat Burn', 'min': 114, 'max': 138}, {'minutes': 0, 'caloriesOut': 0.0, 'name': 'Cardio', 'min': 139, 'max': 169}, {'minutes': 0, 'caloriesOut': 0.0, 'name': 'Peak', 'min': 170, 'max': 220}]}, 'goals': {'caloriesOut': 2677, 'steps': 10000, 'distance': 8.05, 'floors': 10, 'activeMinutes': 30}}
        return summary

    def get_activity_intraday(self, token: str, resource: str, date: str, detail_level: int):
        intraday = None
        if resource == "steps":
            intraday = FileUtility.load_json("src/repositories/mock/data/steps-intraday.json")
        elif resource == "calories":
            intraday = FileUtility.load_json("src/repositories/mock/data/calories-intraday.json")
        return intraday
    
    def get_activity_period(self, token, resource, start_date, end_date):
        period = None
        # if resource == "steps":
        #     period = FileUtility.load_json("src/repositories/mock/data/steps-period.json")
        if resource == "calories":
            period = FileUtility.load_json("src/repositories/mock/data/calories-period.json")
        return period