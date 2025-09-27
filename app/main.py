from fastapi import FastAPI
from app.database import lifespan

from .routers import users, tasks


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)
app.include_router(tasks.router)
