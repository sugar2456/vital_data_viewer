from src.repositories.interface.get_sleep_request_repository_interface import GetSleepRequestRepositoryInterface
from src.utilities.error_response_utility import raise_http_exception
import requests

class GetSleepRequestRepository(GetSleepRequestRepositoryInterface):
    def get_sleep(self, token: str, date: str) -> int:
        summary = {
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
        return summary
    
    def get_sleep_detail(self, token: str, date: str, detail_level: int):

        sleep_list = {
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
        return sleep_list