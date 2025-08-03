import uuid

from pydantic import Field
from supadantic.models import BaseSBModel


class BasicDBModel(BaseSBModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
