from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

from sqlalchemy import select

from app.auth.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.models import User
from app.auth.schemas import RegisterUser
from app.auth.util import create_access_token, get_password_hash, verify_password
from app.database import SessionDep
from fastapi import HTTPException, status


router = APIRouter()


@router.get("/users", tags=["users"])
async def get_users(session: SessionDep):
    users = session.query(User).all()
    return users


@router.post("/register", tags=["users"])
async def register(session: SessionDep, user: RegisterUser):
    existing_user = session.scalar(select(User).where(User.email == user.email))
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    session.add(db_user)
    session.commit()
    return {"msg": "User created successfully"}


@router.post("/login", tags=["users"])
async def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = session.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
