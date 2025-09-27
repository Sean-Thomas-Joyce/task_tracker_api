from typing import Annotated

from fastapi import Depends, HTTPException, status
import jwt
from sqlalchemy import select

from app.auth.constants import ALGORITHM, SECRET_KEY
from app.auth.models import User
from app.auth.schemas import TokenData
from app.database import SessionDep
from app.config import oauth2_scheme


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: SessionDep,
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = session.scalar(select(User).where(User.email == token_data.username))
    if user is None:
        raise credentials_exception
    return user
