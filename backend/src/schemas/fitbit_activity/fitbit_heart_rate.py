from pydantic import BaseModel

class FitbitHeartRateRequest(BaseModel):
    """Fitbitの心拍数取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
    """
    user_id: str
    date: str
    
class FitbitHeartRateResponse(BaseModel):
    """Fitbitの心拍数取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        resting_heart_rate (int): 心拍数
    """
    resting_heart_rate: int

class FitbitHeartRateIntradayRequest(BaseModel):
    """Fitbitの心拍数取得リクエストモデル

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

class FitbitHeartRateIntradayResponse(BaseModel):
    heart_rate_intraday: list