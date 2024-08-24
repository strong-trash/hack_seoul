from dataclasses import dataclass

from command import Command


@dataclass(frozen=True)
class LikeCommand(Command):
    user_id: int
    product_id: int


@dataclass(frozen=True)
class DislikeCommand(Command):
    user_id: int
    product_id: int
