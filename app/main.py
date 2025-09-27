from fastapi import FastAPI
from app.database import lifespan

from app.tasks.router import router as task_router
from app.auth.router import router as auth_router


app = FastAPI(lifespan=lifespan)


app.include_router(auth_router)
app.include_router(task_router)
