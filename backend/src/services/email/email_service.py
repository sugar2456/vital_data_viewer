# FILE: email_service.py
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from src.utilities.error_response_utility import raise_http_exception
from src.config import Settings
from src.services.email.email_service_interface import EmailServiceInterface
from datetime import datetime

class EmailService(EmailServiceInterface):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.mail_username,
            MAIL_PASSWORD=settings.mail_password,
            MAIL_FROM=settings.mail_from,
            MAIL_PORT=settings.mail_port,
            MAIL_SERVER=settings.mail_server,
            MAIL_STARTTLS=settings.mail_starttls,
            MAIL_SSL_TLS=settings.mail_ssl_tls,
            USE_CREDENTIALS=settings.use_credentials,
        )

    async def send_email(self, email: str, subject: str, body: str) -> None:
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype=MessageType.html
        )
        fm = FastMail(self.conf)
        try:
            await fm.send_message(message)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"メール送信に成功しました: {current_time}")
        except Exception as e:
            print(f"メール送信に失敗しました: {e}")
            raise_http_exception(
                status_code=500,
                message="メール送信に失敗しました"
            )