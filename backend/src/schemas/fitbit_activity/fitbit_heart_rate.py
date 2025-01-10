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