from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base


class Product(Base):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(256))
    image_path: Mapped[str] = mapped_column(String(512))
    price: Mapped[int] = mapped_column(Integer)
    summary: Mapped[str] = mapped_column(Text, nullable=True)

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
    like_history: Mapped[list["Like"]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
    carts: Mapped[list["Cart"]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
