# backend/app/api/main.py

from fastapi import APIRouter

from app.api.routes import items, login, users, allocation, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(allocation.router, prefix="/allocation", tags=["allocation"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])  # Add this line
