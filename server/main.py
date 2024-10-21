from fastapi import FastAPI
from asyncpg import create_pool
from contextlib import asynccontextmanager

from routers.v1.urls.router import router as url_router
from configurations import (
    ShardAConfigurations, 
    ShardBConfigurations, 
    ShardCConfigurations
)


POOL_A = POOL_B = POOL_C = None

@asynccontextmanager
async def lifespan(server: FastAPI):
    global POOL_A
    global POOL_B
    global POOL_C

    POOL_A = create_pool(ShardAConfigurations().model_dump())
    POOL_B = create_pool(ShardBConfigurations().model_dump())
    POOL_C = create_pool(ShardCConfigurations().model_dump())

    yield


application = FastAPI(lifespan=lifespan)
application.include_router(url_router)