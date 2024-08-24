from pydantic import BaseModel


class LikeDto(BaseModel):
    user_id: int
    product_id: int

