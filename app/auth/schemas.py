from pydantic import BaseModel

from app.tasks.schemas import Task


class User(BaseModel):
    id: int | None
    email: str
    tasks: list[Task] = []


class UserInDB(User):
    hashed_password: str


class RegisterUser(BaseModel):
    email: str
    password: str
