from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from command.product import AddProductCommand
from depends import get_messagebus, get_session
from depends.product import add_product_command
from dto.product import ProductResponseDto, ProductResponseModel
from messagebus import MessageBus
from service import product as product_service

api = APIRouter()


@api.get("/{product_id}/{user_id}", status_code=status.HTTP_200_OK)
async def show_product(
    product_id: int,
    user_id: int,
    session: Annotated[Session, Depends(get_session)]
) -> ProductResponseDto:
    return await product_service.show_product(
        product_id, user_id, session
    )


@api.get("", status_code=status.HTTP_200_OK)
async def list_product(
    session: Annotated[Session, Depends(get_session)]
) -> ProductResponseModel:
    products = await product_service.list_product(session)

    product_responses = [
        ProductResponseDto.from_entity(product)
        for product in products
    ]

    return ProductResponseModel(products=product_responses)


@api.post("", status_code=status.HTTP_201_CREATED)
async def add_product(
    command: Annotated[AddProductCommand, Depends(add_product_command)],
    messagebus: Annotated[MessageBus, Depends(get_messagebus)]
):
    return await messagebus.handle(command)
