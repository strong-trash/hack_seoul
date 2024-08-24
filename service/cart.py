from sqlalchemy.orm.session import Session

from command.cart import AddCartCommand, DeleteCartCommand, UpdateCartCommand
from exception import BadRequestException, NotFoundException
from orm.cart import Cart
from repository.cart import CartRepository


async def list_cart(
    user_id: int,
    session: Session
):
    repository = CartRepository(session)

    cart_products = repository.get_by_user_id(user_id)
    return cart_products


async def add_cart(
    command: AddCartCommand,
    session: Session
):
    repository = CartRepository(session)
    obj = repository.get_by_user_id_and_product_id(
        user_id=command.user_id,
        product_id=command.product_id
    )
    if obj is None:
        obj = Cart(
            user_id=command.user_id,
            product_id=command.product_id,
            count=1
        )
        repository.add(obj)
    else:
        update_command = UpdateCartCommand(
            cart_id=obj.id,
            count=obj.count + 1
        )
        await update_cart(
            update_command,
            session
        )


async def update_cart(
    command: UpdateCartCommand,
    session: Session
):
    if command.count <= 0:
        raise BadRequestException
    repository = CartRepository(session)
    obj = repository.get_by_id(command.cart_id)
    if obj is None:
        raise NotFoundException
    obj.count = command.count


async def delete_cart(
    command: DeleteCartCommand,
    session: Session,
):
    repository = CartRepository(session)
    obj = repository.get_by_id(command.cart_id)
    if obj is None:
        raise NotFoundException
    repository.delete(obj)
