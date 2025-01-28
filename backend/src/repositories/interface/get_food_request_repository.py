from abc import ABC, abstractmethod

class GetFoodRequestRepositoryInterface(ABC):
    @abstractmethod
    def get_food(self, token: str, date: str) -> dict:
        """食事情報を取得

        Args:
            token (str): アクセストークン
            date (str): 日付

        Returns:
            dict: _description_
        """
        pass
    
    @abstractmethod
    def get_food_period(self, token: str, start_date: str, end_date: str) -> dict:
        """食事情報を取得

        Args:
            token (str): アクセストークン
            start_date (str): 開始日
            end_date (str): 終了日

        Returns:
            dict: _description_
        """
        pass