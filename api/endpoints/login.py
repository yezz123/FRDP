from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import models
from api import deps
from core import security
from core.config import settings
from core.password import generate_password_reset_token, verify_password_reset_token
from core.security import get_password_hash
from crud.crud_user import CRUDUser
from schemas.msg import Msg
from schemas.token import Token
from schemas.user import User

router = APIRouter()

user1 = CRUDUser(User)


@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = user1.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user1.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=User)
def Check_Session(
    current_user: models.user.User = Depends(deps.get_current_user),
) -> Any:
    """
    Test if a user is logged in by checking if a valid access token is in the header
    """
    return current_user


@router.post(
    "/password-recovery/{email}",
    response_model=Msg,
    status_code=200,
    response_description="Success",
)
def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
    """
    Password Recovery
    """
    user = user1.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=422,
            detail="The user with this username does not exist in the system.",
        )
    return {"msg": generate_password_reset_token(email=email)}


@router.post("/reset-password/", response_model=Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset your password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully!"}
