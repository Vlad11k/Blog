import datetime

from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, text, ForeignKey


class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    content: Mapped[str]
    photo: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(
                server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(
                server_default=text("TIMEZONE('utc', now())"),
                onupdate=datetime.datetime.utcnow())
    is_published: Mapped[bool] = mapped_column(default=True)

    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    def __repr__(self):
        return f'{self.id} - {self.title}'