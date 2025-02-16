from sqlalchemy.orm import Session
from src.repositories.mysql_alchemy.users_repository import UserRepository
from src.repositories.mysql_alchemy.pkce_cache_repository import PkceCacheRepository
from src.repositories.mysql_alchemy.user_token_repository import UserTokenRepository
from src.repositories.http.get_activity_request_repository import GetActivityRequestRepository
from src.repositories.http.get_sleep_request_repository import GetSleepRequestRepository
from src.repositories.http.get_heart_rate_request_repository import GetHeartRateRequestRepository
from src.repositories.http.get_body_request_repository import GetBodyRequestRepository
from src.repositories.http.get_devices_request_repository import GetDevicesRequestRepository
from src.repositories.http.get_food_request_repository import GetFoodRequestRepository
from repositories.http.email_repository import EmailRepository
from src.db.session import get_db
from src.config import settings
from fastapi import Depends

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_pkce_cache_repository(db: Session = Depends(get_db)) -> PkceCacheRepository:
    return PkceCacheRepository(db)

def get_user_token_repository(db: Session = Depends(get_db)) -> UserTokenRepository:
    return UserTokenRepository(db)

def get_email_repository() -> EmailRepository:
    return EmailRepository(settings=settings)

def get_activity_request_repository() -> GetActivityRequestRepository:
    return GetActivityRequestRepository()

def get_sleep_request_repository() -> GetSleepRequestRepository:
    return GetSleepRequestRepository()

def get_heart_rate_request_repository() -> GetHeartRateRequestRepository:
    return GetHeartRateRequestRepository()

def get_weight_request_repository() -> GetBodyRequestRepository:
    return GetBodyRequestRepository()

def get_devices_request_repository() -> GetDevicesRequestRepository:
    return GetDevicesRequestRepository()

def get_food_request_repository() -> GetFoodRequestRepository:
    return GetFoodRequestRepository()