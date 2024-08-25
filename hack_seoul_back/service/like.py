from sqlalchemy.orm.session import Session

from command.like import DislikeCommand, LikeCommand
from const import LikeStatus
from orm.like import Like
from repository.like import LikeRepository


async def like(command: LikeCommand, session: Session) -> Like:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=command.user_id, product_id=command.product_id
    )
    if obj is None:
        obj = Like(
            user_id=command.user_id,
            product_id=command.product_id,
            is_like=LikeStatus.LIKE,
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.DISLIKE:
        obj.is_like = LikeStatus.LIKE
    return obj


async def dislike(command: DislikeCommand, session: Session) -> Like:
    repository = LikeRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=command.user_id, product_id=command.product_id
    )
    if obj is None:
        obj = Like(
            user_id=command.user_id,
            product_id=command.product_id,
            is_like=LikeStatus.DISLIKE,
        )
        repository.add(obj)
    elif obj.is_like == LikeStatus.LIKE:
        obj.is_like = LikeStatus.DISLIKE
    return obj
