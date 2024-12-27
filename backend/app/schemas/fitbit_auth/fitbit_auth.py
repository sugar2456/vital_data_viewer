from pydantic import BaseModel

class FitbitAuthRequest(BaseModel):
    fitbit_user_id: str

class FitbitAuthResponse(BaseModel):
    message: str
