import requests
from datetime import datetime, timedelta
from src.utilities.error_response_utility import raise_http_exception

class HttpUtility:
    """HTTP通信ユーティリティ\n
        requestsライブラリを使用してHTTP通信を行う\n
        例外をキャッチしてエラーメッセージを出力する
    """
    @staticmethod
    def get(url: str, headers: dict) -> requests.Response:
        """GETリクエスト

        Args:
            url (str): URL
            headers (dict): ヘッダー

        Returns:
            requests.Response: レスポンス
        """
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP errorが発生: {http_err}')  # HTTPエラー
            if response.status_code == 429:
                now = datetime.now()
                reset_seconds = int(response.headers.get('Fitbit-Rate-Limit-Reset', 3600))
                reset_time = now + timedelta(seconds=reset_seconds)
                
                raise_http_exception(429, f"Fitbit API制限に達しました　リセット時間: {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection errorが発生: {conn_err}')  # 接続エラー
            raise_http_exception(500, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout errorが発生: {timeout_err}')  # タイムアウトエラー
            raise_http_exception(500, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'その他エラーが発生: {req_err}')  # その他のリクエストエラー
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
    
    @staticmethod
    def post(url: str, headers: dict, data: dict) -> requests.Response:
        """POSTリクエスト

        Args:
            url (str): URL
            headers (dict): ヘッダー
            data (dict): データ

        Returns:
            requests.Response: レスポンス
        """
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP errorが発生: {http_err}')  # HTTPエラー
            if response.status_code == 429:
                now = datetime.now()
                reset_seconds = int(response.headers.get('Fitbit-Rate-Limit-Reset', 3600))
                reset_time = now + timedelta(seconds=reset_seconds)
                
                raise_http_exception(429, f"Fitbit API制限に達しました　リセット時間: {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection errorが発生: {conn_err}')  # 接続エラー
            raise_http_exception(500, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout errorが発生: {timeout_err}')  # タイムアウトエラー
            raise_http_exception(500, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'その他エラーが発生: {req_err}')  # その他のリクエストエラー
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
    