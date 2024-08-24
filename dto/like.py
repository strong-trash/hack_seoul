from pydantic import BaseModel

from orm.like import Like


class LikeDto(BaseModel):
    user_id: int
    product_id: int


class LikeResponseDto(BaseModel):
    is_like: int
    user_id: int
    product_id: int

    @staticmethod
    def from_entity(like: Like):
        return LikeResponseDto(
            is_like=like.is_like,
            user_id=like.user_id,
            product_id=like.product_id,
        )
