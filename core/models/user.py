from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .record import Record


class User(Base):
    __tablename__ = "users"
    user_name: Mapped[str] = mapped_column(String(50), unique=True)
    records: Mapped[list["Record"]] = relationship(back_populates="user")
