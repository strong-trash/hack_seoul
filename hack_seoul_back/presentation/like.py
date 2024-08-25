from typing import Annotated

from fastapi import APIRouter, Depends, status

from command.like import DislikeCommand, LikeCommand
from depends import get_messagebus
from depends.like import dislike_command, like_command
from dto.like import LikeResponseDto
from messagebus import MessageBus

api = APIRouter()


@api.post("/like", status_code=status.HTTP_201_CREATED)
async def like(
    command: Annotated[LikeCommand, Depends(like_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)],
) -> LikeResponseDto:
    like_obj = await messagebus.handle(command)

    return LikeResponseDto.from_entity(like_obj)


@api.post("/dislike", status_code=status.HTTP_201_CREATED)
async def dislike(
    command: Annotated[DislikeCommand, Depends(dislike_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)],
) -> LikeResponseDto:
    like_obj = await messagebus.handle(command)

    return LikeResponseDto.from_entity(like_obj)
