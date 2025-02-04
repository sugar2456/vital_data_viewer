from fastapi import APIRouter, Depends
from src.config import settings
from src.services.fitbit.fitbit_auth_service import FitbitAuthService
from src.schemas.fitbit_auth.fitbit_conform import FitbitConformResponse
from src.utilities.error_response_utility import raise_http_exception
from src.api.dependencies import get_pkce_cache_repository, get_user_token_repository, get_user_repository
from src.repositories.interface.pkce_cache_repostiory_interface import PkceCacheRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface


router = APIRouter()

@router.get("/auth/confirm", response_model=FitbitConformResponse)
async def fitbit_auth_confirm(
    code: str,
    state: str,
    pkce_cache_repository: PkceCacheRepositoryInterface = Depends(get_pkce_cache_repository),
    user_repository: UsersRepositoryInterface = Depends(get_user_repository),
    user_token_repository: UserTokenRepositoryInterface = Depends(get_user_token_repository)
) -> FitbitConformResponse:
    # 認証コードを使用してトークンを取得する
    client_id = settings.fitbit_client_id
    client_secret = settings.fitbit_client_secret
    redirect_uri = settings.fitbit_redirect_uri
    
    service = FitbitAuthService(None, pkce_cache_repository, user_repository, user_token_repository)
    isGetToken = service.get_token(client_id, client_secret, redirect_uri, code, state)
    
    if isGetToken:
        return FitbitConformResponse(message="fitbitのリソース許可が完了しました")
    else:
        return raise_http_exception(
            status_code=500,
            message="fitbitのリソース許可に失敗しました"
        )