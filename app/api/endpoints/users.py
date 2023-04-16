from typing import Any

from api.deps import get_current_active_superuser, get_current_active_user, get_db
from base.user import CRUDUser
from core.config import settings
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from models.schema import User, UserCreate, UserUpdate
from models.tables import User as models_user
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

router = APIRouter()

user1 = CRUDUser(User)


@router.post("/", response_model=User)
def create_New_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
    current_user: models_user = Depends(get_current_active_superuser),
) -> Any:
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
    db: Session = Depends(get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models_user = Depends(get_current_active_user),
) -> Any:
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
    db: Session = Depends(get_db),
    current_user: models_user = Depends(get_current_active_user),
) -> Any:
    return current_user


@router.put("/{user_id}", response_model=User)
def update_Other_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserUpdate,
    current_user: models_user = Depends(get_current_active_superuser),
) -> Any:
    user = user1.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = CRUDUser.update(db, db_obj=user, obj_in=user_in)
    return user


@router.post("/Create", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
    password: str = Body(...),
) -> Any:
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
