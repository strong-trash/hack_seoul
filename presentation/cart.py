
from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from depends import get_session
from dto.cart import CartDto, CartResponseDto, CartResponseModel, CartUpdateDto
from exception import BadRequestException, NotFoundException
from orm.cart import Cart
from repository.cart import CartRepository

api = APIRouter()


@api.get("/{user_id}", status_code=status.HTTP_200_OK)
async def list_shoppingcart(
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> CartResponseModel:
    repository = CartRepository(session)

    cart_products = repository.get_by_user_id(user_id)
    products = [
        CartResponseDto.from_entity(cart_product)
        for cart_product in cart_products
    ]
    return CartResponseModel(
        products=products
    )


@api.post("", status_code=status.HTTP_201_CREATED)
async def add_shoppingcart(
    cart: CartDto,
    session: Annotated[Session, Depends(get_session)]
) -> CartDto:
    repository = CartRepository(session)
    obj = Cart(
        user_id=cart.user_id,
        product_id=cart.product_id,
        count=1
    )
    repository.add(obj)
    return cart


@api.put("/{cart_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_shoppingcart(
    cart_id: int,
    cart: CartUpdateDto,
    session: Annotated[Session, Depends(get_session)]
) -> CartUpdateDto:
    if cart.count <= 0:
        raise BadRequestException
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    obj.count = cart.count

    return cart


@api.delete("/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shoppingcart(
    cart_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> None:
    repository = CartRepository(session)
    obj = repository.get_by_id(cart_id)
    if obj is None:
        raise NotFoundException
    repository.delete(obj)
