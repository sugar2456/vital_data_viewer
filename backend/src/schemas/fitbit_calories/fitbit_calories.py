from pydantic import BaseModel
from typing import List

class FitbitCaloriesPeriodResponse(BaseModel):
    """Fitbitの消費カロリーと歩数取得レスポンスモデル(詳細)

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    calories_period: List