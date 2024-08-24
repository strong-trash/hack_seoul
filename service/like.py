

from sqlalchemy.orm.session import Session

from const import LikeStatus
from dto.like import LikeDto
from orm.like import Like
from repository.like import LikeRepository


async def like(
    like_data: LikeDto,
    session: Session
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


async def dislike(
    like_data: LikeDto,
    session: Session
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
