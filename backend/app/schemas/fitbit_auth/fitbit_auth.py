from pydantic import BaseModel

class FitbitAuthRequest(BaseModel):
    user_email: str

class FitbitAuthResponse(BaseModel):
    message: str
