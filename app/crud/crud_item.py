import uuid

from sqlmodel import Session

from app.crud.base import BaseService
from app.models.comment import Comment, CommentCreate, CommentUpdate


class CommentService(BaseService[Comment, CommentCreate, CommentUpdate]):
    def create(
        self, session: Session, *, owner_id: uuid.UUID, obj_in: CommentCreate
    ) -> Comment:
        return super().create(session, owner_id=owner_id, obj_in=obj_in)

    # def update(
    #     self, session: Session, *, id: uuid.UUID, obj_in: CommentUpdate
    # ) -> Comment | None:
    #     return super().update(session, id=id, obj_in=obj_in)


item = CommentService(Comment)
