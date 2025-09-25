from fastapi import APIRouter

from app.database import SessionDep


router = APIRouter()


@router.post("/register", tags=["users"])
async def register(session: SessionDep):
    pass


@router.post("/login", tags=["users"])
async def login(session: SessionDep):
    pass
