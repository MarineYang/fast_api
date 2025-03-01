

from typing import Any
from config.config import web_server_config
from fastapi.responses import ORJSONResponse
from fastapi.security import HTTPBearer

from commons.utils.enums import EXCEPTION_INVALID_CLIENT_ACCESS


security = HTTPBearer()


async def IsWebServer():
    if True == web_server_config.is_web_server:
        raise EXCEPTION_INVALID_CLIENT_ACCESS
    

def RemoveNoneValues(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: RemoveNoneValues(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [RemoveNoneValues(v) for v in obj]
    return obj

def RemoveNoneResponse(obj):
    return ORJSONResponse(content=RemoveNoneValues(obj.dict()))
