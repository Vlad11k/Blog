from typing import List

from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from models.post import Post


class Category(db.Model):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(50), unique=True)

    posts: Mapped[List['Post']] = relationship()

    def __repr__(self):
        return f'{self.id} - {self.name}'
