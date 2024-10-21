from fastapi import APIRouter, status

from routers.v1.urls.service import Service
from routers.v1.urls.scheme import (
    GetResponse, 
    PostRequest, 
    PostResponse
)


router = APIRouter(prefix="/urls", tags=["URLS"])


@router.get(path="/{url_id}", response_model=GetResponse, status_code=status.HTTP_200_OK)
async def get(url_id: str):
    # get neccessary pool
    return await Service(db).get(url_id=url_id)


@router.post(path="", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create(request: PostRequest):
    # get neccessary pool
    return await Service(db).create(request=request)