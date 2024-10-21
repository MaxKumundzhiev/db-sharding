from typing import Any

from asyncpg import Pool

from routers.v1.urls.scheme import (
    GetResponse,
    PostRequest,
    PostResponse
)


class Service:
    def __init__(self, pool: Pool, shard: int | Any | tuple | None) -> None:
        self.pool: Pool = pool
        self.shard: Pool = shard
    
    async def get(url_id: str) -> GetResponse:
        return GetResponse(id="xyz123", url="abc", url_id=url_id)

    async def post(request: PostRequest) -> PostResponse:
        raise NotImplementedError