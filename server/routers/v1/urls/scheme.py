from pydantic import BaseModel


class PostRequest(BaseModel):
    url: str


class PostResponse(BaseModel):
    id: str
    url: str
    url_id: str
    shard_id: str


class GetResponse(BaseModel):
    id: str
    url: str
    url_id: str