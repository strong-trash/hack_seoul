from pydantic import BaseModel

from orm.cart import Cart


class CartDto(BaseModel):
    user_id: int
    product_id: int


class CartUpdateDto(BaseModel):
    count: int


class CartResponseDto(BaseModel):
    id: int | None
    count: int
    name: str | None
    image_path: str | None
    price: int | None

    @staticmethod
    def from_entity(cart: Cart):
        product = cart.product
        return CartResponseDto(
            id=cart.id,
            count=cart.count,
            name=product and product.name,
            image_path=product and product.image_path,
            price=product and product.price,
        )


class CartResponseModel(BaseModel):
    products: list[CartResponseDto]
