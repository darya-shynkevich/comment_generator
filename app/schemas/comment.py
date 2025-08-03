from pydantic import BaseModel

from app.models.comment import CommentBase


class CommentRequest(BaseModel):
    keywords: list[str]


class CommentResponse(CommentBase):
    pass
