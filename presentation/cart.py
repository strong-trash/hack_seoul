
from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from command.cart import AddCartCommand, DeleteCartCommand, UpdateCartCommand
from depends import get_messagebus, get_session
from depends.cart import (add_cart_command, delete_cart_command,
                          update_cart_command)
from dto.cart import CartResponseDto, CartResponseModel
from messagebus import MessageBus
from service import cart as cart_service

api = APIRouter()


@api.get("/{user_id}", status_code=status.HTTP_200_OK)
async def list_cart(
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> CartResponseModel:
    cart_products = await cart_service.list_cart(
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
async def add_cart(
    command: Annotated[AddCartCommand, Depends(add_cart_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)]
):
    return await messagebus.handle(command)


@api.put("/{cart_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_cart(
    command: Annotated[UpdateCartCommand, Depends(update_cart_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)]
):
    return await messagebus.handle(command)


@api.delete("/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(
    command: Annotated[DeleteCartCommand, Depends(delete_cart_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)]
) -> None:
    await messagebus.handle(command)
