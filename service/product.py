from sqlalchemy.orm.session import Session

from const import LikeStatus
from dto.product import ProductDto, ProductResponseDto
from orm.product import Product
from repository.like import LikeRepository
from repository.product import ProductRepository


async def show_product(
    product_id: int,
    user_id: int,
    session: Session,
):
    product_repository = ProductRepository(session)
    like_repository = LikeRepository(session)
    product = product_repository.get_greater_than_id(product_id)
    if product is None:
        product = product_repository.get_greater_than_id(0)

    likes = like_repository.get_by_product_id(product.id)
    like_user_ids = [
        like.user_id for like in likes if like.is_like == LikeStatus.LIKE
    ]
    dislike_user_ids = [
        like.user_id for like in likes if like.is_like == LikeStatus.DISLIKE
    ]
    
    return ProductResponseDto.from_entity(
        product=product,
        like_count=len(like_user_ids),
        dislike_count=len(dislike_user_ids),
        is_like=user_id in like_user_ids,
        is_dislike=user_id in dislike_user_ids
    )


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
