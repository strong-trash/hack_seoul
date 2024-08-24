from typing import Annotated

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm.session import Session

from const import LikeStatus
from depends import get_session
from dto.like import LikeDto
from orm.like import Like
from repository.like import LikeRepository

api = APIRouter()

@api.post("/like", status_code=status.HTTP_201_CREATED)
async def like(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )
    if obj is None:
        obj = Like(
            user_id=like_data.user_id,
            product_id=like_data.product_id,
            is_like=LikeStatus.LIKE
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.DISLIKE:
        obj.is_like = LikeStatus.LIKE

    return like_data


@api.post("/dislike", status_code=status.HTTP_201_CREATED)
async def dislike(
    like_data: LikeDto,
    session: Annotated[Session, Depends(get_session)]
) -> LikeDto:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )
    if obj is None:
        obj = Like(
            user_id=like_data.user_id,
            product_id=like_data.product_id,
            is_like=LikeStatus.DISLIKE
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.LIKE:
        obj.is_like = LikeStatus.DISLIKE

    return like_data
