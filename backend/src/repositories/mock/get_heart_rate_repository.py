from src.repositories.interface.get_heart_rate_request_repository_interface import GetHeartRateRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetHeartRateRequestRepository(GetHeartRateRequestRepositoryInterface):
    def get_heart_rate(self, token: str, date: str) -> int:
        heart_rate = {
            "resting_heart_rate": 65
        }
        return heart_rate
    
    def get_heart_rate_intraday(self, token: str, date: str, detail_level: int):
        heart_rate_intraday = {
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

        return heart_rate_intraday