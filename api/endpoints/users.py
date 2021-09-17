from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps
from core.config import settings
from crud.crud_user import CRUDUser
from schemas.user import User, UserCreate, UserUpdate

router = APIRouter()

user1 = CRUDUser(User)


@router.post("/", response_model=User)
def create_New_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserCreate,
    current_user: models.user.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = user1.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user1.create(db, obj_in=user_in)
    return user


@router.put("/me", response_model=User)
def update_Current_User(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    return user1.update(db, db_obj=current_user, obj_in=user_in)


@router.get("/me", response_model=User)
def Get_Current_User_by_ID(
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.put("/{user_id}", response_model=User)
def update_Other_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: UserUpdate,
    current_user: models.user.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = user1.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.post("/Create", response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
    password: str = Body(...),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = user1.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = UserCreate(password=password, email=email, full_name=full_name)
    user = user1.create(db, obj_in=user_in)
    return user
