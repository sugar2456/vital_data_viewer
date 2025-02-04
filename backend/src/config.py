from pydantic import BaseSettings

class Settings(BaseSettings):
    fitbit_client_id: str
    fitbit_client_secret: str
    fitbit_redirect_uri: str
    fitbit_authorization_uri: str
    fitbit_refresh_token_uri: str
    db_username: str
    db_hostname: str
    db_port: int
    db_name: str
    db_charset: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_server: str
    mail_port: int
    mail_starttls: bool
    mail_ssl_tls: bool
    use_credentials: bool
    validate_certs: bool
    secret_key: str
    secret_algorithm: str

    class Config:
        env_file = ".env"

settings = Settings()