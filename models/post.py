from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    content: Mapped[str]
    photo: Mapped[str] = mapped_column(String(255))
    is_published: Mapped[bool] = mapped_column(default=True)