from fastapi import HTTPException
from enum import Enum, auto


class ErrorType(Enum):
    SUCCESS = 0
    FAIL = 1

    DB_RUN_FAILED = 10
    DB_ALREADY_SAME_KEY = auto()
    DB_INVALID_KEY = auto()
    DB_EMPTY_DATA = auto()
    DB_NOT_EMPTY_DATA = auto()
    DB_INVALID_TYPE = auto()
    DB_NOT_MATCHED_DATA = auto()
    REDIS_RUN_FAILED = auto()

    JSON_PARSE_ERROR = 100
    INVALID_REQEUST_DATA = auto()
    INTERAL_EXCEPTION = auto()

    # 서버 상태 에러
    SERVER_CLOSE = 110
    SERVER_MAINTENANCE = auto()

    # 서버 통신 에러
    SERVER_BROADCAST_NOT_USED = 150

    # http 에러 코드랑 겹치지 않도록 설정 - router 전용 예외 발생 옵션임
    HTTP_INVALID_CLIENT_REQUEST = 419
    HTTP_TO_MANY_REQUEST = 429
    HTTP_INVALID_CLIENT_ACCESS = 433
    HTTP_ACCESS_TOKEN_EXPIRED = 434
    HTTP_REFRESH_TOKEN_EXPIRED = 435
    HTTP_INVALID_TOKEN_ACCESS = 436

    # 컨텐츠 관련 에러
    CONTENTS_INVALID_SEASON_DAY_ROUND_KEY = 500



# ErrorType 숫자와 중복되면 안됨
EXCEPTION_INVALID_CLIENT_REQUEST = HTTPException(status_code=ErrorType.HTTP_INVALID_CLIENT_REQUEST.value, detail=ErrorType.HTTP_INVALID_CLIENT_REQUEST.name)
EXCEPTION_TO_MANY_REQUEST = HTTPException(status_code=ErrorType.HTTP_TO_MANY_REQUEST.value, detail=ErrorType.HTTP_TO_MANY_REQUEST.name)
EXCEPTION_INVALID_CLIENT_ACCESS = HTTPException(status_code=ErrorType.HTTP_INVALID_CLIENT_ACCESS.value, detail=ErrorType.HTTP_INVALID_CLIENT_ACCESS.name)
EXCEPTION_ACCESS_TOKEN_EXPIRED = HTTPException(status_code=ErrorType.HTTP_ACCESS_TOKEN_EXPIRED.value, detail=ErrorType.HTTP_ACCESS_TOKEN_EXPIRED.name)
EXCEPTION_REFRESH_TOKEN_EXPIRED = HTTPException(status_code=ErrorType.HTTP_REFRESH_TOKEN_EXPIRED.value, detail=ErrorType.HTTP_REFRESH_TOKEN_EXPIRED.name)
EXCEPTION_HTTP_INVALID_TOKEN_ACCESS = HTTPException(status_code=ErrorType.HTTP_INVALID_TOKEN_ACCESS.value, detail=ErrorType.HTTP_INVALID_TOKEN_ACCESS.name)
# Socket Server Protocol Enums