from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base


class Like(Base):
    __tablename__ = "like_history"

    is_like: Mapped[str] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))

    product: Mapped["Product"] = relationship(back_populates="like_history")
    user: Mapped["User"] = relationship(back_populates="like_history")
