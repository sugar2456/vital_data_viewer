from fastapi import APIRouter
from app.config import settings
from app.services.fitbit.fitbit_auth_service import FitbitAuthService
from app.services.email.email_service import EmailService
from app.schemas.fitbit_auth.fitbit_auth import FitbitAuthRequest, FitbitAuthResponse
from app.schemas.fitbit_auth.fitbit_conform import FitbitConformRequest, FitbitConformResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests
import base64

router = APIRouter()

@router.post("/fitbit/auth", response_model=FitbitAuthResponse)
async def fitbit_auth(request: FitbitAuthRequest) -> FitbitAuthResponse:
    # configから取得
    client_id = settings.fitbit_client_id
    client_secret = settings.fitbit_client_secret
    redirect_uri = settings.fitbit_redirect_uri
    
    # userにfitbitのリソース許可を求める
    email_service = EmailService(settings)
    service = FitbitAuthService(email_service)
    await service.get_allow_user_resource(client_id, client_secret, redirect_uri)
    
    return FitbitAuthResponse(message="メール送信成功")

@router.get("/auth/confirm", response_model=FitbitConformResponse)
async def fitbit_auth_confirm(code: str, state: str) -> FitbitConformResponse:
    print(f"code: {code}")
    print(f"state: {state}")
    
    if code:
        # 認証コードを使用してトークンを取得する
        client_id = settings.fitbit_client_id
        client_secret = settings.fitbit_client_secret
        redirect_uri = settings.fitbit_redirect_uri
        authorization = f"{client_id}:{client_secret}"
        base64encoded = base64.b64encode(authorization.encode()).decode()
        authorization_header = f"Basic {base64encoded}"
        
        headers = {
            'Authorization': authorization_header,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'client_id': client_id,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code,
            'code_verifier': 'your_code_verifier'  # ここに実際のcode_verifierを設定してください
        }
        
        response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)
        
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            return JSONResponse(content={"error": "トークン取得に失敗しました", "details": response.json()}, status_code=response.status_code)
    else:
        return JSONResponse(content={"error": "認証コードが見つかりませんでした"}, status_code=400)