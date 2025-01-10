import urllib.parse
from src.utilities.error_response_utility import raise_http_exception
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
        user_repository: UsersRepositoryInterface,
        user_token_repository: UserTokenRepositoryInterface
    ):
        self.email_service = email_service
        self.pkce_cache_repository = pkce_cache_repository
        self.user_repository = user_repository
        self.user_token_repository = user_token_repository

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
            await self.email_service.send_email(user_email, "fitbitのリソース許可のお願い", authorize_url)
        
        except Exception as e:
            print(f"send email error: {e}")
            raise_http_exception(
                status_code=500,
                message="メール送信に失敗しました"
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
        state: str
    ) -> bool:
        """トークンURLの取得

        Args:
            client_id (str): fitbitのクライアントID
            client_secret (str): fitbitのクライアントシークレット
            redirect_uri (str): fitbitのリダイレクトURI
            code (str): 認証コード
            state (str): state

        Returns:
            bool: 成功したかどうか
        """
        
        try:
            authorization = f"{client_id}:{client_secret}"
            base64encoded = base64.b64encode(authorization.encode()).decode()
            authorization_header = f"Basic {base64encoded}"
            code_verifier = ''
            
            # code_verifierをキャッシュから取得する
            code_verifier = self.pkce_cache_repository.get_pkce_cache(state).code_verifier
            
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
            if response.status_code == 200:
                user_id = response.json()['user_id']
                access_token = response.json()['access_token']
                refresh_token = response.json()['refresh_token']
                token_type = response.json()['token_type']
                expires_in = response.json()['expires_in']
                
                system_user_id = self.user_repository.get_user_by_fitbit_user_id(user_id).id
                
                new_user_token = UserToken(
                    user_id=system_user_id,
                    access_token=access_token,
                    refresh_token=refresh_token,
                    token_type=token_type,
                    expires_in=expires_in
                )
                self.user_token_repository.create_user_token(new_user_token)
                return True
            else:
                return False
        except Exception as e:
            print(f"get token error: {e}")
            raise_http_exception(
                status_code=500,
                message="fitbitのリソース許可に失敗しました"
            )

    def refresh_access_token(
        self,
        refresh_token: str,
        client_id: str,
        client_secret: str,
    ) -> str:
        """リフレッシュトークンを使用して新しいアクセストークンを取得

        Args:
            refresh_token (str): リフレッシュトークン
            client_id (str): クライアントID
            client_secret (str): クライアントシークレット

        Returns:
            str: 新しいアクセストークン
        """
        url = "https://api.fitbit.com/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token_data = response.json()
            print(token_data)
            new_fitbit_user_id = token_data["user_id"]
            new_token_type = token_data["token_type"]
            new_access_token = token_data["access_token"]
            new_refresh_token = token_data["refresh_token"]
            new_expires_in = token_data["expires_in"]
            user = self.user_repository.get_user_by_fitbit_user_id(new_fitbit_user_id)
            new_user_token = UserToken(
                user_id=user.id,
                token_type=new_token_type,
                access_token=new_access_token,
                refresh_token=new_refresh_token,
                expires_in=new_expires_in
            )
            updated_user_token = self.user_token_repository.update_user_token(new_user_token)
            if updated_user_token:
                return updated_user_token.access_token
            else:
                raise_http_exception(
                    status_code=500,
                    message="アクセストークンのリフレッシュに失敗しました"
                )
        else:
            raise_http_exception(
                status_code=500,
                message="アクセストークンのリフレッシュに失敗しました"
            )