from pydantic import BaseModel

from orm.product import Product


class ProductDto(BaseModel):
    name: str
    image_path: str
    price: int
    summary: str | None = None


class ProductResponseDto(ProductDto):
    id: int | None
    like_count: int | None
    dislike_count: int | None
    is_like: bool | None
    is_dislike: bool | None

    @staticmethod
    def from_entity(
        product: Product,
        like_count: int | None = None,
        dislike_count: int | None = None,
        is_like: bool | None = None,
        is_dislike: bool | None = None,
    ):
        return ProductResponseDto(
            id=product.id,
            name=product.name,
            image_path=product.image_path,
            price=product.price,
            summary=product.summary,
            like_count=like_count,
            dislike_count=dislike_count,
            is_like=is_like,
            is_dislike=is_dislike,
        )


class ProductResponseModel(BaseModel):
    products: list[ProductResponseDto]
