from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base


class Cart(Base):
    __tablename__ = "shopping_cart"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
    count: Mapped[int] = mapped_column(Integer)

    product: Mapped["Product"] = relationship(back_populates="carts")
    user: Mapped["User"] = relationship(back_populates="carts")
