from asyncpg import Pool

from routers.v1.urls.scheme import (
    GetResponse,
    PostRequest,
    PostResponse
)


class Service:
    def __init__(self, db: Pool) -> None:
        self.db: Pool = db
    
    async def get(url_id: str) -> GetResponse:
        raise NotImplementedError

    async def post(request: PostRequest) -> PostResponse:
        raise NotImplementedError