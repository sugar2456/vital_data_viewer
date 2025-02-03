import pytest
from unittest.mock import AsyncMock, patch
from src.repositories.http.email_repository import EmailRepository
from src.config import Settings
from dotenv import load_dotenv
import os

@pytest.fixture(scope="session", autouse=True)
def load_test_env():
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.testing'))

@pytest.fixture
def settings():
    return Settings()

@pytest.fixture
def email_repository(settings) -> EmailRepository:
    return EmailRepository(settings)


@pytest.mark.asyncio
async def test_send_email_success(email_repository):
    with patch("src.repositories.http.email_repository.FastMail.send_message", new_callable=AsyncMock) as mock_send_message:
        await email_repository.send_email("test@gmail.com", "Test Subject", "Test Body")
        mock_send_message.assert_called_once()
        args, kwargs = mock_send_message.call_args
        assert args[0].subject == "Test Subject"
        assert args[0].recipients == ["test@gmail.com"]
        assert args[0].body == "Test Body"

@pytest.mark.asyncio
async def test_send_email_failure(email_repository):
    with patch("src.repositories.http.email_repository.FastMail.send_message", new_callable=AsyncMock) as mock_send_message:
        mock_send_message.side_effect = Exception("SMTP server error")
        with pytest.raises(Exception, match="500: .*メール送信に失敗しました.*"):
            await email_repository.send_email("test@gmail.com", "Test Subject", "Test Body")