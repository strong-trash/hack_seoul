from command.like import DislikeCommand, LikeCommand
from dto.like import LikeDto


async def like_command(like_data: LikeDto):
    return LikeCommand(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )


async def dislike_command(like_data: LikeDto):
    return DislikeCommand(
        user_id=like_data.user_id,
        product_id=like_data.product_id
    )
