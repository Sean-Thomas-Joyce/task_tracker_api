from fastapi import APIRouter

router = APIRouter()


@router.post("/register", tags=["users"])
async def register():
    pass


@router.post("/login", tags=["users"])
async def login():
    pass
