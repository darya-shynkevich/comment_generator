import uuid

from pydantic import Field
from supadantic.models import BaseSBModel

from app.models.base import BasicDBModel


class CommentBase(BaseSBModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class Comment(BasicDBModel, CommentBase):
    __tablename__ = "comments"
    __table_args__ = {
        "schema": "public",
        "keep_existing": True
    }


class CommentPublic(CommentBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class ItemsPublic(BaseSBModel):
    data: list[CommentPublic]
    count: int
