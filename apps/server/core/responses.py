from typing import Any, Optional
from pydantic import BaseModel

class APIResponse(BaseModel):
    data: Optional[Any] = None
    error: Optional[str] = None
    message: str = "success"

def success_response(data: Any = None, message: str = "success") -> dict:
    return {
        "data": data,
        "error": None,
        "message": message
    }

def error_response(error_code: str, message: str, data: Any = None) -> dict:
    return {
        "data": data,
        "error": error_code,
        "message": message
    }
