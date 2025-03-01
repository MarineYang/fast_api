from fastapi import APIRouter, Depends, Path

from router.v1.open_ai.protocol import Res_OpenAIInfo
from router.v1.validator.dependencies import IsWebServer, RemoveNoneResponse
from services.open_ai_services import OpenAiService



router = APIRouter(prefix="/v1/open_ai", dependencies=[Depends(IsWebServer)], tags=["Open AI"], responses={404: {"description": "Not found"}})

@router.get(
    path="/get/value",
    # dependencies=[Depends(IsValidAccessToken)],
    response_model=Res_OpenAIInfo,
    summary="open ai get value",
    description="open ai get value. 오픈 ai 값 가져오기",
)
async def get_open_ai_value(service: OpenAiService = Depends()):
    return RemoveNoneResponse(await service.get_open_ai_value())
