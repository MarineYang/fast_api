from fastapi import FastAPI
import os
import sys
import uvicorn
from config.config import web_server_config




if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(
                "router.router:app",
                host=web_server_config.host,
                port=web_server_config.port,
                access_log=False,
                # workers=web_server_config.process_count,
                # ssl_keyfile="./SSL/dev/key.pem",
                # ssl_certfile="./SSL/dev/cert.pem",
                # ssl_keyfile=os.path.join(os.path.dirname(__file__), "./SSL/dev/key.pem"),
                # ssl_certfile=os.path.join(os.path.dirname(__file__), "./SSL/dev/cert.pem"),
            )
    

