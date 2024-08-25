from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base


class Review(Base):
    __tablename__ = "review"

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    comment: Mapped[int] = mapped_column(Text)

    product: Mapped["Product"] = relationship(back_populates="reviews")
