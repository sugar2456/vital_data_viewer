from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: str
    updated_at: str

class UsersResponse(BaseModel):
    users: List[User]

class UserCreatedRequest(BaseModel):
    name: str
    email: str
    fitbit_user_id: str
    role: str

class UserCreatedResponse(BaseModel):
    created: bool
    user: User