from fastapi import FastAPI
from routers.v1.urls.router import router as url_router


application = FastAPI()

application.include_router(url_router)