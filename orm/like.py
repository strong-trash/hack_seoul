from orm.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Like(Base):
    __tablename__ = "like_history"

    is_like: Mapped[str] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))

    product: Mapped["Product"] = relationship(back_populates="like_history")
    user: Mapped["User"] = relationship(back_populates="like_history")
