from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list():
    pass


@router.post("/tasks")
async def create(task: dict):
    pass


@router.get("/tasks/{task_id}")
async def retrieve(task_id: int):
    pass


@router.put("/tasks/{task_id}")
async def update(task_id: int, updated_task: dict):
    pass


@router.delete("/tasks/{task_id}")
async def delete(task_id: int):
    pass
