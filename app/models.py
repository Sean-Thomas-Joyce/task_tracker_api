from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str


class Task(BaseModel):
    id: int | None
    title: str
    description: str | None = None
    user_id: int


class User(BaseModel):
    id: int | None
    email: str
    tasks: list[Task] = []


class UserInDB(User):
    hashed_password: str


class RegisterUser(BaseModel):
    email: str
    password: str
