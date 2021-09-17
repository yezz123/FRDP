from fastapi import APIRouter

from api.endpoints import login, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
