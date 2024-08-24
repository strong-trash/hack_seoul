from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from depends import get_session
from dto.like import LikeDto
from service import like as like_service

api = APIRouter()


@api.post("/like", status_code=status.HTTP_201_CREATED)
async def like(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    await like_service.like(like_data, session)

    return like_data


@api.post("/dislike", status_code=status.HTTP_201_CREATED)
async def dislike(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    await like_service.dislike(like_data, session)

    return like_data
