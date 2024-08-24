
from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from depends import get_session
from dto.cart import CartDto, CartResponseDto, CartResponseModel, CartUpdateDto
from service import cart as cart_service

api = APIRouter()


@api.get("/{user_id}", status_code=status.HTTP_200_OK)
async def list_shoppingcart(
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> CartResponseModel:
    cart_products = await cart_service.list_shoppingcart(
        user_id, session
    )

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
    await cart_service.add_shoppingcart(cart, session)
    return cart


@api.put("/{cart_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_shoppingcart(
    cart_id: int,
    cart: CartUpdateDto,
    session: Annotated[Session, Depends(get_session)]
) -> CartUpdateDto:
    await cart_service.update_shoppingcart(cart_id, cart, session)

    return cart


@api.delete("/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shoppingcart(
    cart_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> None:
    await cart_service.delete_shoppingcart(
        cart_id, session
    )
