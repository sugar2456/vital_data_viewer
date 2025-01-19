from pydantic import BaseModel

class FitbitWeightRequest(BaseModel):
    """Fitbitの体重取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        date (str): 取得日
    """
    user_id: str
    date: str

class FitbitWeightResponse(BaseModel):
    """Fitbitの体重取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    weight: float
    bmi: float
    fat: float
    date: str
    
class FitbitWeightPeriodRequest(BaseModel):
    """Fitbitの体重期間取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
        start_date (str): 取得開始日
        end_date (str): 取得終了日
    """
    user_id: str
    start_date: str
    end_date: str

class FitbitWeightPeriodResponse(BaseModel):
    """Fitbitの体重取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    weight_list: list