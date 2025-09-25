from fastapi import APIRouter

from app.database import SessionDep


router = APIRouter()


@router.get("/tasks")
async def list(session: SessionDep):
    pass


@router.post("/tasks")
async def create(task: dict, session: SessionDep):
    pass


@router.get("/tasks/{task_id}")
async def retrieve(task_id: int, session: SessionDep):
    pass


@router.put("/tasks/{task_id}")
async def update(task_id: int, updated_task: dict, session: SessionDep):
    pass


@router.delete("/tasks/{task_id}")
async def delete(task_id: int, session: SessionDep):
    pass
