import requests

class HttpUtility:
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
            response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # HTTPエラー
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')  # 接続エラー
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')  # タイムアウトエラー
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')  # その他のリクエストエラー
    
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
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')  # 接続エラー
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')  # タイムアウトエラー
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')  # その他のリクエストエラー