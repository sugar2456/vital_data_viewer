from fastapi import HTTPException
from src.schemas.commons.error_response import ErrorResponse

def raise_http_exception(status_code: int, message: str):
    error_response = ErrorResponse(
        detail="エラーが発生しました",
        code=status_code,
        message=message
    )
    raise HTTPException(
        status_code=status_code,
        detail=error_response.dict()
    )
