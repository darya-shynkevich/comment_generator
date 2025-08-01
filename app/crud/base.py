import uuid
from collections.abc import Sequence
from typing import Generic, TypeVar

from sqlmodel import Session, SQLModel, select

from app.models.base import BasicDBModel

ModelType = TypeVar("ModelType", bound=BasicDBModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        """ CRUD object with default methods to Create, Read, Update, Delete (CRUD). """
        self.model: BasicDBModel = model

    def get(self, session: Session, *, id: uuid.UUID) -> ModelType | None:
        """Get a single record by id"""
        statement = select(self.model).where(self.model.id == id)
        result = session.exec(statement)
        return result.one_or_none()

    def get_multi(
        self, session: Session, *, skip: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        """Get multiple records with pagination"""
        statement = select(self.model).offset(skip).limit(limit)
        result = session.exec(statement)
        return result.all()

    def create(
        self, session: Session, *, owner_id: uuid.UUID, obj_in: CreateSchemaType
    ) -> ModelType:
        db_obj = self.model.objects.create(
            **dict(owner_id=owner_id, **obj_in.model_dump())
        )
        # db_obj = self.model()
        # session.add(db_obj)
        # session.commit()
        # session.refresh(db_obj)
        return db_obj

    # def update(
    #     self, session: Session, *, id: uuid.UUID, obj_in: UpdateSchemaType
    # ) -> ModelType | None:
    #     """Update existing record"""
    #     db_obj = self.get(session, id=id)
    #     if db_obj:
    #         update_data = obj_in.model_dump(exclude_unset=True)
    #         db_obj.sqlmodel_update(update_data)
    #
    #         session.add(db_obj)
    #         session.commit()
    #         session.refresh(db_obj)
    #     return db_obj
    #
    # def remove(self, session: Session, *, id: uuid.UUID) -> ModelType | None:
    #     """Remove a record"""
    #     obj = self.get(session, id=id)
    #     if obj:
    #         session.delete(obj)
    #         session.commit()
    #     return obj
