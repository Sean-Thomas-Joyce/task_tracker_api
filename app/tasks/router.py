from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.auth.dependencies import get_current_user
from app.database import SessionDep
from app.tasks.models import Task
from app.tasks.schemas import Task as TaskSchema


router = APIRouter()


@router.get("/tasks", tags=["tasks"], response_model=list[TaskSchema])
async def list(session: SessionDep, current_user=Depends(get_current_user)):
    stmt = select(Task).where(Task.user_id == current_user.id)
    tasks = session.execute(stmt).scalars().all()
    return tasks


@router.get("/tasks/{task_id}", tags=["tasks"])
async def retrieve(
    task_id: int, session: SessionDep, current_user=Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if task and task.user_id == current_user.id:
        return task
    return None


@router.post("/tasks", tags=["tasks"])
async def create(
    task_data: TaskSchema, session: SessionDep, current_user=Depends(get_current_user)
):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        user_id=current_user.id,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.put("/tasks/{task_id}", tags=["tasks"])
async def update(
    task_id: int,
    updated_task: TaskSchema,
    session: SessionDep,
    current_user=Depends(get_current_user),
):
    task = session.get(Task, task_id)
    if task and task.user_id == current_user.id:
        task.title = updated_task.title
        task.description = updated_task.description
        session.commit()
        session.refresh(task)
        return task
    return None


@router.delete("/tasks/{task_id}", tags=["tasks"])
async def delete(
    task_id: int, session: SessionDep, current_user=Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if task and task.user_id == current_user.id:
        session.delete(task)
        session.commit()
        return task
    return None
