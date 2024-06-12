from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, select

from models.post import Post
from models.models import Base, db


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(50), unique=True)

    posts: Mapped[List['Post']] = relationship()

    def __repr__(self):
        return f'{self.id} - {self.name}'
