from pydantic import Field
from supadantic.models import BaseSBModel

from app.models.base import BasicDBModel


class CommentBase(BaseSBModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None)


class Comment(BasicDBModel, CommentBase):
    __table_args__ = {"schema": "public", "keep_existing": True}
