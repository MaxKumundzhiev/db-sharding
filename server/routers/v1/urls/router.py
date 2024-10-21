from fastapi import APIRouter, status

from routers.v1.urls.service import Service
from routers.v1.urls.scheme import (
    GetResponse, 
    PostRequest, 
    PostResponse
)
from core.sharding.consistent_hashing import get_hash_ring


router = APIRouter(prefix="/urls", tags=["URLS"])


@router.get(path="/{url_id}", response_model=GetResponse, status_code=status.HTTP_200_OK)
async def get(url_id: str):
    return await Service(None, None).get(url_id=url_id)


@router.post(path="", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create(request: PostRequest):
    raise NotImplemented