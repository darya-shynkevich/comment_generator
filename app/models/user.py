import uuid

from pydantic import EmailStr, Field
from supadantic.models import BaseSBModel


class User(BaseSBModel):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth", "keep_existing": True}
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(max_length=255)
