from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    email_verified_at: Optional[str]
    role: int

class UsersResponse(BaseModel):
    users: List[User]

class UserCreatedRequest(BaseModel):
    name: str
    email: str
    fitbit_user_id: str
    role: int

class UserCreatedResponse(BaseModel):
    created: bool
    user: User