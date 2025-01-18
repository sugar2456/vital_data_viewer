from src.repositories.interface.get_step_request_repository_interface import GetStepRequestRepositoryInterface
from src.utilities.http_utility import HttpUtility
from src.utilities.error_response_utility import raise_http_exception

class GetStepRequestRepository(GetStepRequestRepositoryInterface):
    def get_step(self, token: str, date: str) -> int:
        steps = 10000
        return steps

    def get_step_intraday(self, token: str, date: str, detail_level: int):
        step_intraday = {
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
        ]}
        return step_intraday