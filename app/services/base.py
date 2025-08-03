from collections.abc import Sequence
from typing import Generic, TypeVar

from app.models.base import BasicDBModel

ModelType = TypeVar("ModelType", bound=BasicDBModel)


class BaseService(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        """CRUD object with default methods to Create, Read, Update, Delete (CRUD)."""
        self.model: BasicDBModel = model

    def list(self, *, offset: int = 0, limit: int = 100) -> Sequence[ModelType]:
        """Get multiple records with pagination"""
        return self.model.objects.all()[offset : offset + limit]
