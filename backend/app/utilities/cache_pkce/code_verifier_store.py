from abc import ABC, abstractmethod

class CodeVerifierStore(ABC):
    """pkce codeを保存する
    """
    @abstractmethod
    def save_code_verifier(self, email: str, code_verifier: str):
        pass

    @abstractmethod
    def get_code_verifier(self, email: str) -> str:
        pass

    @abstractmethod
    def delete_code_verifier(self, email: str):
        pass