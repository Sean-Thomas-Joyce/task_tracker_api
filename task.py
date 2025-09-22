from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Tasks(BaseModel):
    id: int
    description: str
    status: Status
    created_at: datetime
    updated_at: datetime
