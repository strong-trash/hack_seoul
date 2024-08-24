from pydantic import BaseModel


class ProductDto(BaseModel):
    name: str
    image_path: str
    price: int
    summary: str | None = None
