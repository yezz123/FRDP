from datetime import timedelta
from typing import Any

from api.deps import get_current_user, get_db
from base.user import CRUDUser
from core.config import settings
from extension.password import verify_password_reset_token
from extension.security import create_access_token, get_password_hash
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.schema import Msg, Token, User
from models.tables import User as models_user
from sqlalchemy.orm import Session

router = APIRouter()

user1 = CRUDUser(User)


@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = user1.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user1.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=User)
def Check_Session(
    current_user: models_user = Depends(get_current_user),
) -> Any:
    return current_user


@router.post(
    "/password-recovery/{email}",
    response_model=Msg,
    status_code=200,
    response_description="Success",
)
def recover_password(email: str, db: Session = Depends(get_db)) -> Any:
    user = user1.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=422,
            detail="The user with this username does not exist in the system.",
        )
    raise HTTPException(
        status_code=200,
        detail=f"An email with instructions to reset your password has been sent to {email}",
    )


@router.post("/reset-password/", response_model=Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(get_db),
) -> Any:
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = CRUDUser.get_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    raise HTTPException(status_code=200, detail="Password updated successfully")
