from fastapi import APIRouter

from app.database import SessionDep
from app.models import Task as TaskSchema
from app.tables.models import Task


router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def list(session: SessionDep):
    tasks = session.query(Task).all()
    return tasks


@router.post("/tasks", tags=["tasks"])
async def create(task_data: TaskSchema, session: SessionDep):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        user_id=task_data.user_id,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("/tasks/{task_id}", tags=["tasks"])
async def retrieve(task_id: int, session: SessionDep):
    return session.get(Task, task_id)


@router.put("/tasks/{task_id}", tags=["tasks"])
async def update(task_id: int, updated_task: TaskSchema, session: SessionDep):
    task = session.get(Task, task_id)
    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        session.commit()
        session.refresh(task)
    return task


@router.delete("/tasks/{task_id}", tags=["tasks"])
async def delete(task_id: int, session: SessionDep):
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
    return task
