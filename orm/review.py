from orm.base import Base
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Review(Base):
    __tablename__ = "review"

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    comment: Mapped[int] = mapped_column(Text)

    product: Mapped["Product"] = relationship(back_populates="reviews")
