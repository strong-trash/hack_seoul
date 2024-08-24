from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from depends import get_session
from dto.product import ProductDto, ProductResponseDto, ProductResponseModel
from service import product as product_service

api = APIRouter()


@api.get("/{product_id}", status_code=status.HTTP_200_OK)
async def show_product(
    product_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    product = await product_service.show_product(
        product_id, session
    )
    return product


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
    product: ProductDto,
    session: Annotated[Session, Depends(get_session)]
) -> ProductDto:
    await product_service.add_product(
        product, session
    )
    return product
