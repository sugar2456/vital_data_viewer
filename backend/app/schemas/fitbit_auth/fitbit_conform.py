from pydantic import BaseModel

class FitbitConformRequest(BaseModel):
    code: str
    state: str

class FitbitConformResponse(BaseModel):
    message: str