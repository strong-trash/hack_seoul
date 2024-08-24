from orm.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Cart(Base):
    __tablename__ = "shopping_cart"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
    count: Mapped[int] = mapped_column(Integer)

    product: Mapped["Product"] = relationship(back_populates="carts")
    user: Mapped["User"] = relationship(back_populates="carts")
