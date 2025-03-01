from router.v1.open_ai.protocol import Res_OpenAIInfo

class OpenAiService:
    def __init__(self):
        pass

    async def get_open_ai_value(self) -> Res_OpenAIInfo:

        res = Res_OpenAIInfo()

        res.uid = 1
        return res