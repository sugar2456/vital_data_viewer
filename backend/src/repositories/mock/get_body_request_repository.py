from src.repositories.interface.get_body_request_repository_interface import GetBodyRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetBodyRequestRepository(GetBodyRequestRepositoryInterface):
    def get_body(self, token: str, date: str) -> dict:
        response = {
            "weight": 62.2,
            "bmi": 23.7,
            "fat": 19.5,
            "date": "2024-12-15"
        }
        return response
        
    
    def get_body_period(self, token: str, start_date: str, end_date: str) -> dict:
        body_period = [
            {
                "bmi": 23.62,
                "date": "2025-01-03",
                "fat": 19.700000762939453,
                "logId": 1735943951000,
                "source": "API",
                "time": "22:39:11",
                "weight": 62
            },
            {
                "bmi": 23.59,
                "date": "2025-01-04",
                "fat": 19.399999618530273,
                "logId": 1736028843000,
                "source": "API",
                "time": "22:14:03",
                "weight": 61.9
            },
            {
                "bmi": 23.51,
                "date": "2025-01-05",
                "fat": 19,
                "logId": 1736115640000,
                "source": "API",
                "time": "22:20:40",
                "weight": 61.7
            },
            {
                "bmi": 23.85,
                "date": "2025-01-06",
                "fat": 20.100000381469727,
                "logId": 1736204138000,
                "source": "API",
                "time": "22:55:38",
                "weight": 62.6
            },
            {
                "bmi": 23.7,
                "date": "2025-01-07",
                "fat": 19.600000381469727,
                "logId": 1736288847000,
                "source": "API",
                "time": "22:27:27",
                "weight": 62.2
            },
            {
                "bmi": 23.62,
                "date": "2025-01-09",
                "fat": 19.600000381469727,
                "logId": 1736466176000,
                "source": "API",
                "time": "23:42:56",
                "weight": 62
            },
            {
                "bmi": 23.7,
                "date": "2025-01-10",
                "fat": 19.600000381469727,
                "logId": 1736548562000,
                "source": "API",
                "time": "22:36:02",
                "weight": 62.2
            },
            {
                "bmi": 22.63,
                "date": "2025-01-11",
                "fat": 18.700000762939453,
                "logId": 1736635525000,
                "source": "API",
                "time": "22:45:25",
                "weight": 59.4
            },
            {
                "bmi": 23.85,
                "date": "2025-01-13",
                "logId": 1736809042000,
                "source": "API",
                "time": "22:57:22",
                "weight": 62.6
            },
            {
                "bmi": 23.93,
                "date": "2025-01-13",
                "fat": 20,
                "logId": 1736809080000,
                "source": "API",
                "time": "22:58:00",
                "weight": 62.8
            },
            {
                "bmi": 23.09,
                "date": "2025-01-14",
                "fat": 19.899999618530273,
                "logId": 1736890502000,
                "source": "API",
                "time": "21:35:02",
                "weight": 60.6
            }
        ]
        
        return body_period