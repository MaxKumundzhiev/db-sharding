from fastapi import APIRouter, status

from routers.v1.urls.scheme import (
    GetResponse, PostRequest, PostResponse
)

router = APIRouter(prefix="/urls", tags=["URLS"])


@router.get(path="/{id}", response_model=GetResponse, status_code=status.HTTP_200_OK)
async def get(id: str):
    raise NotImplementedError


@router.post(path="", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create(request: PostRequest):
    raise NotImplementedError