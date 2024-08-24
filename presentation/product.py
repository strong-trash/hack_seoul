from fastapi import APIRouter, status, Depends

from typing import Annotated

from sqlalchemy.orm.session import Session

from depends import get_session
from dto.product import ProductDto, ProductResponseDto, ProductResponseModel
from orm.product import Product
from repository.product import ProductRepository

api = APIRouter()


@api.get("/{product_id}", status_code=status.HTTP_200_OK)
async def show_product(
    product_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    repository = ProductRepository(session)
    product = repository.get_greater_than_id(product_id)
    if product is None:
        product = repository.get_greater_than_id(0)
    return product


@api.get("", status_code=status.HTTP_200_OK)
async def list_product(
    session: Annotated[Session, Depends(get_session)]
) -> ProductResponseModel:
    repository = ProductRepository(session)
    products = repository.get_all()

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
    repository = ProductRepository(session)
    obj = Product(
        name=product.name,
        image_path=product.image_path,
        price=product.price,
        summary=product.summary
    )
    repository.add(obj)
    return product
