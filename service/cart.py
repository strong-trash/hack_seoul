from sqlalchemy.orm.session import Session

from dto.cart import CartDto, CartUpdateDto
from exception import BadRequestException, NotFoundException
from orm.cart import Cart
from repository.cart import CartRepository


async def list_shoppingcart(
    user_id: int,
    session: Session
):
    repository = CartRepository(session)

    cart_products = repository.get_by_user_id(user_id)
    return cart_products


async def add_shoppingcart(
    cart: CartDto,
    session: Session
):
    repository = CartRepository(session)
    obj = Cart(
        user_id=cart.user_id,
        product_id=cart.product_id,
        count=1
    )
    repository.add(obj)


async def update_shoppingcart(
    cart_id: int,
    cart: CartUpdateDto,
    session: Session
):
    if cart.count <= 0:
        raise BadRequestException
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    obj.count = cart.count


async def delete_shoppingcart(
    cart_id: int,
    session: Session,
):
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    repository.delete(obj)
