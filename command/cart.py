from dataclasses import dataclass

from command import Command


@dataclass(frozen=True)
class AddCartCommand(Command):
    user_id: int
    product_id: int


@dataclass(frozen=True)
class UpdateCartCommand(Command):
    cart_id: int
    count: int


@dataclass(frozen=True)
class DeleteCartCommand(Command):
    cart_id: int
