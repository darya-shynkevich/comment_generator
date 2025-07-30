from fastapi import APIRouter

from app.api.routes import comments, utils

api_router = APIRouter()
api_router.include_router(items.router)
api_router.include_router(utils.router)
