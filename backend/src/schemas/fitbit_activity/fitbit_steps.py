from pydantic import BaseModel
from typing import List, Dict

class FitbitActivityRequest(BaseModel):
    """Fitbitのアクティビティ取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
    """
    user_id: str
    date: str

class FitbitActivityResponse(BaseModel):
    """Fitbitのアクティビティ取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        activity (Dict): アクティビティ
    """
    activity: Dict

class FitbitStepsRequest(BaseModel):
    """Fitbitの歩数取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
    """
    user_id: str
    date: str

class FitbitStepsResponse(BaseModel):
    """Fitbitの歩数取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        steps (int): 歩数
    """
    steps: int

class FitbitStepsIntradayRequest(BaseModel):
    """Fitbitの歩数取得リクエストモデル(詳細)

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
        detail_level (int): 詳細レベル
    """
    user_id: str
    date: str
    detail_level: int

class FitbitStepsIntradayResponse(BaseModel):
    """Fitbitの歩数取得レスポンスモデル(詳細)

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    steps_intraday: List
    
class FitbitCaloriesIntradayResponse(BaseModel):
    """Fitbitの消費カロリー取得レスポンスモデル(詳細)

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    calories_intraday: List