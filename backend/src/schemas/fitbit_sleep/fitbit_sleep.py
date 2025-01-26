from pydantic import BaseModel
from typing import List, Optional, Union

class FitbitSleepRequest(BaseModel):
    """Fitbitの睡眠取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
    """
    user_id: str
    date: str

class SleepStages(BaseModel):
    deep: int
    light: int
    rem: int
    wake: int

class FitbitSleepResponse(BaseModel):
    """Fitbitの睡眠取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    stages: SleepStages
    totalMinutesAsleep: int
    totalSleepRecords: int
    totalTimeInBed: int

class FitbitSleepDetailRequest(BaseModel):
    """Fitbitの睡眠取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
        detail_level (str): 取得詳細レベル
    """
    user_id: str
    date: str
    detail_level: str

class SleepLevelData(BaseModel):
    dateTime: str
    level: str
    seconds: int

class SleepSummaryDetail(BaseModel):
    count: int
    minutes: int
    thirtyDayAvgMinutes: Optional[int] = None

class SleepSummaryClassicDetail(BaseModel):
    count: int
    minutes: int

class SleepStageSummary(BaseModel):
    deep: SleepSummaryDetail
    light: SleepSummaryDetail
    rem: SleepSummaryDetail
    wake: SleepSummaryDetail

class SleepStageSummaryClassic(BaseModel):
    restless: SleepSummaryClassicDetail
    asleep: SleepSummaryClassicDetail
    awake: SleepSummaryClassicDetail

class SleepLevels(BaseModel):
    data: List[SleepLevelData]
    shortData: Optional[List[SleepLevelData]] = []
    summary: Union[SleepStageSummary, SleepStageSummaryClassic]


class SleepRecord(BaseModel):
    dateOfSleep: str
    duration: int
    efficiency: int
    endTime: str
    infoCode: int
    isMainSleep: bool
    levels: SleepLevels
    logId: int
    minutesAfterWakeup: int
    minutesAsleep: int
    minutesAwake: int
    minutesToFallAsleep: int
    logType: str
    startTime: str
    timeInBed: int
    type: str

class FitbitSleepDetailResponse(BaseModel):
    sleep: List[SleepRecord]