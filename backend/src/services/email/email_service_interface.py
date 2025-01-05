from abc import ABC, abstractmethod

class EmailServiceInterface(ABC):
    @abstractmethod
    async def send_email(self, email: str, subject: str, body: str) -> None:
        """メールを送信

        Args:
            email (str): emailアドレス
            subject (str): 件名
            body (str): 本文
        """
        pass