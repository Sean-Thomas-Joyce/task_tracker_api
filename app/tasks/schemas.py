from pydantic import BaseModel


class Task(BaseModel):
    id: int | None
    title: str
    description: str | None = None
    user_id: int
