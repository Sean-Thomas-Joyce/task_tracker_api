from pydantic import BaseModel

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str
