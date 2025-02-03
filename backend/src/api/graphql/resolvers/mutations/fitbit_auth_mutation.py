import strawberry
from typing import Optional
from src.config import settings
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.services.email.email_service import EmailRepository

@strawberry.type
class FitbitAuthMutation:
    @strawberry.mutation
    async def fitbit_auth(self, fitbit_user_id: str) -> Optional[str]:
        # configから取得
        client_id = settings.fitbit_client_id
        client_secret = settings.fitbit_client_secret
        redirect_uri = settings.fitbit_redirect_uri
        
        # userにfitbitのリソース許可を求める
        email_service = EmailRepository(settings)
        service = FitbitAuthService(email_service)
        access_token = await service.get_allow_user_resource(client_id, client_secret, redirect_uri)
        
        return None