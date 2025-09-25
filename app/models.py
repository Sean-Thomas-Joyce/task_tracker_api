from pydantic import BaseModel


class Task(BaseModel):
    id: int | None
    title: str
    description: str | None = None
    user_id: int


class User(BaseModel):
    id: int | None
    username: str
    email: str
    tasks: list[Task]
