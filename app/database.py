from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.models import Base


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
