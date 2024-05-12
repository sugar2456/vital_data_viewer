import os

from typing import List
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from app.config import Settings

class EmailSchema(BaseModel):
    email: List[EmailStr]

html = """
<p>Thanks for using Fastapi-mail</p> 
"""

async def simple_send(email: EmailSchema, settings: Settings) -> JSONResponse:
    conf = ConnectionConfig(
        MAIL_USERNAME = settings.mail_username,
        MAIL_PASSWORD = settings.mail_password,
        MAIL_FROM = settings.mail_from,
        MAIL_PORT = settings.mail_port,
        MAIL_SERVER = settings.mail_server,
        MAIL_STARTTLS = settings.mail_starttls,
        MAIL_SSL_TLS = settings.mail_ssl_tls,
        USE_CREDENTIALS = settings.use_credentials,
    )

    message = MessageSchema(
        subject="send test email",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})