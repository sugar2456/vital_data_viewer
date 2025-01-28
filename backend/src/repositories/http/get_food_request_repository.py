from src.repositories.interface.get_food_request_repository import GetFoodRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetFoodRequestRepository(GetFoodRequestRepositoryInterface):
    def get_food(self, token: str, date: str) -> dict:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        url = f"https://api.fitbit.com/1/user/-/foods/log/date/{date}.json"
        
        response = HttpUtility.get(url, headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        
        if not response.json():
            raise_http_exception(500, "摂取食糧情報が取得できませんでした")

        return response.json()

    def get_food_period(self, token: str, start_date: str, end_date: str) -> dict:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        url = f"https://api.fitbit.com/1/user/-/foods/log/caloriesIn/date/{start_date}/{end_date}.json"
        
        response = HttpUtility.get(url, headers)
        if response.status_code != 200:
            raise_http_exception(500, "通信に失敗しました")
        
        if not response.json():
            raise_http_exception(500, "摂取食糧情報が取得できませんでした")
        
        return response.json()