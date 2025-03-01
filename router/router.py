import asyncio
import os
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from typing import Any
from config.config import web_server_config
from commons.utils.gtime import GTime
import router.v1.open_ai.open_ai


form = GTime.UTC().strftime("%Y-%m-%d %H:%M:%S")
API_SERVER_START_TIME = form


# router description
# https://scshim.tistory.com/575
app = FastAPI(title="Project Insta Api Server")

# require client reqeust add header 'Accept-Encoding: gzip'
# body 1000 bytes upper gzip compressed
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get(path="/healthz", responses={404: {"description": "Not found"}})
async def healthz():
    return API_SERVER_START_TIME



app.include_router(router.v1.open_ai.open_ai.router)