import urllib.parse
from fastapi import HTTPException, status
from src.utilities.http_utility import HttpUtility
from src.utilities.pkce_utility import generate_code_verifier, generate_code_challenge, generate_state
from src.services.email.email_service_interface import EmailServiceInterface
from src.repositories.interface.pkce_cache_repostiory_interface import PkceCacheRepositoryInterface
from src.models.pkce_cache import PkceCache

class FitbitAuthService:
    def __init__(self, email_service: EmailServiceInterface, pkce_cache_repository: PkceCacheRepositoryInterface):
        self.email_service = email_service
        self.pkce_cache_repository = pkce_cache_repository

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

    
    def get_code_from_redirect_url(self, redirect_url: str) -> str:
        """リダイレクトURLから認証コードを取得

        Args:
            redirect_url (str): リダイレクトURL

        Returns:
            str: 認証コード
        """
        
        code = redirect_url.split("?code=")[1]
        return code
    
    def get_token(self, client_id: str, client_secret: str, redirect_uri: str, code: str) -> str:
        """トークンURLの取得

        Args:
            client_id (str): fitbitのクライアントID
            client_secret (str): fitbitのクライアントシークレット
            redirect_uri (str): fitbitのリダイレクトURI
            code (str): 認証コード

        Returns:
            str: トークンURL
        """
        
        token_url = "https://api.fitbit.com/oauth2/token"
        headers = {
            "Authorization": f"Basic {client_id}:{client_secret}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "client_id": client_id,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "code": code
        }
        return HttpUtility.post(token_url, headers, data)
