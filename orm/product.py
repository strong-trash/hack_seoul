from orm.base import Base
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Product(Base):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(256))
    image_url: Mapped[str] = mapped_column(String(512))
    price: Mapped[int] = mapped_column(Integer)
    summary: Mapped[int] = mapped_column(Text)

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
    like_history: Mapped[list["Like"]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
