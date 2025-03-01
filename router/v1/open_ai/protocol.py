from pydantic import BaseModel, Field
from commons.models.gmodel import Res_WebPacketProtocol, WebPacketProtocol


class OpenAIProtocol(WebPacketProtocol):
    pass

class Res_OpenAIInfo(Res_WebPacketProtocol):
    """
    response search Oepn AI info
    """
    uid: int = Field(0, description="user uid.", format="int64")
    # uid: int = Field(0, description="user uid.", format="int64")
    # nickname: str = Field("", description="user nickname.")
    # level: int = Field(0, description="user level.")
    # exp: int = Field(0, description="user experience.")
    # grade: int = Field(0, description="user grade.")
    # like: int = Field(0, description="user like count.", format="int64")
    # is_like: bool = Field(False, description="user pick like?")
    # introduction: str = Field("", description="user introduction text.")
    # info_open: bool = Field(False, description="user statistics information open.")
    # analysis_room: list[AnalysisRoom] = Field([], description="user create analysis room list.")
    # goods_list: list[ItemInfo] = Field([], description="보유 재화 정보 리스트.")