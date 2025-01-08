from pydantic import BaseModel

class FitbitAuthRequest(BaseModel):
    """ユーザ認証処理リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_name (str): ユーザ名
        user_email (str): ユーザメールアドレス
        hashed_password (str): ハッシュ化されたパスワード
        fitbit_user_id (str): fitbitユーザID
    """
    user_name: str
    user_email: str
    hashed_password: str
    fitbit_user_id: str

class FitbitAuthResponse(BaseModel):
    message: str
