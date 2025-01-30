from pydantic import BaseModel
from typing import List

class FitbitFoodResponse(BaseModel):
    foods: List

class FitbitFoodPeriodItem(BaseModel):
    date: str
    foods: List

class FitbitFoodPeriodResponse(BaseModel):
    foods_period: List[FitbitFoodPeriodItem]

