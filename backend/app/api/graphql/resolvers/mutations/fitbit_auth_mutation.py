import strawberry
from typing import Optional
from app.config import settings
from app.services.fitbit.fitbit_auth_service import FitbitAuthService
from app.services.email.email_service import EmailService

@strawberry.type
class FitbitAuthMutation:
    @strawberry.mutation
    async def fitbit_auth(self, fitbit_user_id: str) -> Optional[str]:
        # configから取得
        client_id = settings.fitbit_client_id
        client_secret = settings.fitbit_client_secret
        redirect_uri = settings.fitbit_redirect_uri
        
        # ログを出力
        print(f"client_id: {client_id}")
        print(f"client_secret: {client_secret}")
        print(f"redirect_uri: {redirect_uri}")
        print(f"fitbit_user_id: {fitbit_user_id}")
        
        # userにfitbitのリソース許可を求める
        email_service = EmailService(settings)
        service = FitbitAuthService(email_service)
        access_token = await service.get_allow_user_resource(client_id, client_secret, redirect_uri)
        
        print(f"access_token: {access_token}")
        
        return None