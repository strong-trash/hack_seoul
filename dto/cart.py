from pydantic import BaseModel

from orm.cart import Cart


class CartDto(BaseModel):
    user_id: int
    product_id: int


class CartUpdateDto(BaseModel):
    count: int


class CartResponseDto(BaseModel):
    id: int
    name: str
    image_path: str
    price: int
    count: int

    @staticmethod
    def from_entity(cart: Cart):
        product = cart.product
        return CartResponseDto(
            id=cart.id,
            name=product.name,
            image_path=product.image_path,
            price=product.price,
            count=cart.count
        )


class CartResponseModel(BaseModel):
    products: list[CartResponseDto]
