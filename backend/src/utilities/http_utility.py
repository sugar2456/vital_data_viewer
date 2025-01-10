import requests
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
            print(url)
            print(headers)
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # HTTPエラー
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')  # 接続エラー
            raise_http_exception(500, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')  # タイムアウトエラー
            raise_http_exception(500, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')  # その他のリクエストエラー
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
            response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # HTTPエラー
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')  # 接続エラー
            raise_http_exception(500, "Fitbit APIに接続できませんでした")
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')  # タイムアウトエラー
            raise_http_exception(500, "Fitbit APIへのリクエストがタイムアウトしました")
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')  # その他のリクエストエラー
            raise_http_exception(500, "Fitbit APIからデータを取得できませんでした")
    