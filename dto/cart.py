from pydantic import BaseModel


class CartDto(BaseModel):
    user_id: int
    product_id: int


class CartUpdateDto(BaseModel):
    count: int
