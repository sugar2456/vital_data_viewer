from pydantic import BaseModel

class FitbitDevicesRequest(BaseModel):
    """Fitbitのデバイス取得リクエストモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        user_id (str): ユーザID
    """
    user_id: str

class FitbitDevicesInfo(BaseModel):
    """Fitbitのデバイス情報モデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        id (str): デバイスID
        batteryLevel (str): バッテリー残量
        device_version (str): 製品名
        battery (int): バッテリー残量
        last_sync_time (str): 最終同期日時
    """
    id: str
    battery_level: str
    device_version: str
    last_sync_time: str

class FitbitDevicesResponse(BaseModel):
    """Fitbitのデバイス取得レスポンスモデル

    Args:
        BaseModel (_type_): pydanticのBaseModelを継承
    
    properties:
        devices (list): デバイス情報リスト
    """
    devices: list[FitbitDevicesInfo]
    