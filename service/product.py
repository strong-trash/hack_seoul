from sqlalchemy.orm.session import Session

from dto.product import ProductDto
from orm.product import Product
from repository.product import ProductRepository


async def show_product(
    product_id: int,
    session: Session,
):
    repository = ProductRepository(session)
    product = repository.get_greater_than_id(product_id)
    if product is None:
        product = repository.get_greater_than_id(0)
    return product


async def list_product(
    session: Session,
):
    repository = ProductRepository(session)
    products = repository.get_all()

    return products


async def add_product(
    product: ProductDto,
    session: Session
):
    repository = ProductRepository(session)
    obj = Product(
        name=product.name,
        image_path=product.image_path,
        price=product.price,
        summary=product.summary
    )
    repository.add(obj)
