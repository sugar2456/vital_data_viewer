import urllib.parse
from fastapi import HTTPException, status
from src.utilities.http_utility import HttpUtility
from src.utilities.pkce_utility import generate_code_verifier, generate_code_challenge, generate_state
from src.services.email.email_service_interface import EmailServiceInterface
from src.repositories.interface.pkce_cache_repostiory_interface import PkceCacheRepositoryInterface
from src.repositories.interface.users_repository_interface import UsersRepositoryInterface
from src.repositories.interface.user_token_repository_interface import UserTokenRepositoryInterface
from src.models.pkce_cache import PkceCache
from src.models.user import User
from src.models.user_token import UserToken
import requests
import base64

class FitbitAuthService:
    def __init__(
        self,
        email_service: EmailServiceInterface,
        pkce_cache_repository: PkceCacheRepositoryInterface,
        user_repository: UsersRepositoryInterface
    ):
        self.email_service = email_service
        self.pkce_cache_repository = pkce_cache_repository
        self.user_repository = user_repository

    async def get_allow_user_resource(self, client_id:str, user_email: str, redirect_uri: str) -> str:    
        """ユーザーにfitbitのリソース許可を求める

        Args:
            client_id (str): 新規登録するfitbitのクライアントID
            user_email (str): email adress
            redirect_uri (str): fitbitのリダイレクトURI

        Returns:
            None: なし
        """
        
        try:
            # 認証urlを取得
            authorize_url = self.get_authorize_url(client_id, redirect_uri)
            print(f"send email:authorize_url: {authorize_url}")
            
            await self.email_service.send_email(user_email, "fitbitのリソース許可のお願い", authorize_url)
        
        except Exception as e:
            print(f"send email error: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="メールの送信に失敗しました。再試行してください。"
            )
        
        return None

    def get_authorize_url(self, client_id: str, row_redirect_uri: str) -> str:
        """認証URLの取得

        Args:
            client_id (str): 新規登録するfitbitのクライアントID
            redirect_uri (str): fitbitのリダイレクトURI

        Returns:
            str: 認証URL
        """
        code_verifier = generate_code_verifier()
        print(f"code_verifier生成: {code_verifier}")

        row_scope = "activity heartrate location nutrition profile settings sleep social weight"
        scope = urllib.parse.quote(row_scope)
        redirect_uri = urllib.parse.quote(row_redirect_uri)
        state = generate_state()
        code_challenge = generate_code_challenge(code_verifier)
        # code_verifierをキャッシュに保存する処理を追加
        pkce_cache = PkceCache(
            code_verifier=code_verifier,
            state=state
        )
        self.pkce_cache_repository.create_pkce_cache(pkce_cache)

        authorize_url = "https://www.fitbit.com/oauth2/authorize"
        params = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "scope": scope,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "state": state
        }
        
        return authorize_url + "?" + "&".join([f"{key}={value}" for key, value in params.items()])
    
    def get_token(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        code: str,
        state: str,
        user_token_repository: UserTokenRepositoryInterface
    ):
        """トークンURLの取得

        Args:
            client_id (str): fitbitのクライアントID
            client_secret (str): fitbitのクライアントシークレット
            redirect_uri (str): fitbitのリダイレクトURI
            code (str): 認証コード
            state (str): state
            user_token_repository (UserTokenRepositoryInterface): UserTokenRepositoryInterfaceのインスタンス

        Returns:
            str: 
        """
        if code:
            authorization = f"{client_id}:{client_secret}"
            base64encoded = base64.b64encode(authorization.encode()).decode()
            authorization_header = f"Basic {base64encoded}"
            code_verifier = ''
            
            # code_verifierをキャッシュから取得する
            code_verifier = self.pkce_cache_repository.get_pkce_cache(state).code_verifier
            
            print(f"code_verifier: {code_verifier}")
            
            headers = {
                'Authorization': authorization_header,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            data = {
                'client_id': client_id,
                'grant_type': 'authorization_code',
                'redirect_uri': redirect_uri,
                'code': code,
                'code_verifier': code_verifier
            }
            
            response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)
            print(f"response code: {response.status_code}")
            print(f"response message: {response.text}")
            if response.status_code == 200:
                user_id = response.json()['user_id']
                access_token = response.json()['access_token']
                refresh_token = response.json()['refresh_token']
                token_type = response.json()['token_type']
                expires_in = response.json()['expires_in']
                print(f"user_id: {user_id}")
                print(f"access_token: {access_token}")
                print(f"refresh_token: {refresh_token}")
                print(f"token_type: {token_type}")
                print(f"expires_in: {expires_in}")
                
                system_user_id = self.user_repository.get_user_by_fitbit_user_id(user_id).id
                
                new_user_token = UserToken(
                    user_id=system_user_id,
                    access_token=access_token,
                    refresh_token=refresh_token,
                    token_type=token_type,
                    expires_in=expires_in
                )
                user_token_repository.create_user_token(new_user_token)
                return None
            else:
                return None
        else:
            return None
