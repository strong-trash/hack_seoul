from pydantic import BaseModel

from orm.product import Product


class ProductDto(BaseModel):
    name: str
    image_path: str
    price: int
    summary: str | None = None


class ProductResponseDto(ProductDto):
    id: int

    @staticmethod
    def from_entity(product: Product):
        return ProductResponseDto(
            id=product.id,
            name=product.name,
            image_path=product.image_path,
            price=product.price,
            summary=product.summary
        )


class ProductResponseModel(BaseModel):
    products: list[ProductResponseDto]
