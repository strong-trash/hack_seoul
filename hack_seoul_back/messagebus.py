from collections import deque

from sqlalchemy.orm.session import Session

from command import Command
from command.cart import AddCartCommand, DeleteCartCommand, UpdateCartCommand
from command.like import DislikeCommand, LikeCommand
from command.product import AddProductCommand
from service.cart import add_cart, delete_cart, update_cart
from service.like import dislike, like
from service.product import add_product

Message = Command


class MessageBus:
    def __init__(self, session: Session):
        self.session = session
        self.message_queue = None
        self.command_handlers = COMMAND_HANDLERS

    async def handle(self, message: Message):
        self.message_queue = deque([message])
        while self.message_queue:
            target = self.message_queue.popleft()
            ret = await self.handle_command(target)
        return ret

    async def handle_command(self, command: Command):
        handler = self.command_handlers[type(command)]
        return await handler(command, self.session)


COMMAND_HANDLERS = {
    AddCartCommand: add_cart,
    UpdateCartCommand: update_cart,
    DeleteCartCommand: delete_cart,
    LikeCommand: like,
    DislikeCommand: dislike,
    AddProductCommand: add_product,
}
