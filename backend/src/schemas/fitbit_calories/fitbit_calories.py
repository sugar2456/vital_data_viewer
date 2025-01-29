from pydantic import BaseModel
from typing import List

class FitbitCaloriesPeriodResponse(BaseModel):
    """Fitbitの消費カロリーと歩数取得レスポンスモデル(詳細)

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    """
    consumed_calories_period: List
    intaked_calories_period: List
    total_calories_period: List
    