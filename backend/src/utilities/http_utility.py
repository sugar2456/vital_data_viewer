import requests
from datetime import datetime, timedelta
from src.utilities.error_response_utility import raise_http_exception
from src.constants.status_codes import StatusCodes
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
            print(f'HTTP errorが発生: {http_err}')
            if response.status_code == StatusCodes.TOO_MANY_REQUESTS:
                now = datetime.now()
                reset_seconds = int(response.headers.get('Fitbit-Rate-Limit-Reset', 3600))
                reset_time = now + timedelta(seconds=reset_seconds)
                
                raise_http_exception(StatusCodes.TOO_MANY_REQUESTS, f"Fitbit API制限に達しました　リセット時間: {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
            raise_http_exception(StatusCodes.INTERNAL_SERVER_ERROR, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'接続エラーが発生: {conn_err}')
            raise_http_exception(StatusCodes.BAD_GATEWAY, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'タイムアウトが発生: {timeout_err}')
            raise_http_exception(StatusCodes.GATEWAY_TIMEOUT, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'その他エラーが発生: {req_err}')
            raise_http_exception(StatusCodes.INTERNAL_SERVER_ERROR, "Fitbit APIからデータを取得できませんでした")
    
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
            print(f'HTTP errorが発生: {http_err}')
            if response.status_code == StatusCodes.TOO_MANY_REQUESTS:
                now = datetime.now()
                reset_seconds = int(response.headers.get('Fitbit-Rate-Limit-Reset', 3600))
                reset_time = now + timedelta(seconds=reset_seconds)
                
                raise_http_exception(StatusCodes.TOO_MANY_REQUESTS, f"Fitbit API制限に達しました　リセット時間: {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
            raise_http_exception(StatusCodes.INTERNAL_SERVER_ERROR, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'接続エラーが発生: {conn_err}')
            raise_http_exception(StatusCodes.BAD_GATEWAY, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'タイムアウトが発生: {timeout_err}')
            raise_http_exception(StatusCodes.GATEWAY_TIMEOUT, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'その他エラーが発生: {req_err}')
            raise_http_exception(StatusCodes.INTERNAL_SERVER_ERROR, "Fitbit APIからデータを取得できませんでした")
    