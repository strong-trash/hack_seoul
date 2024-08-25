from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(256))

    like_history: Mapped[list["Like"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    carts: Mapped[list["Cart"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
