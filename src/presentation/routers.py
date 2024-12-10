from fastapi import APIRouter

from src.presentation.api.auth_login import auth_router, login_router
from src.configs.urls import URLPathsConfig

api_router = APIRouter()

api_router.include_router(auth_router, prefix=URLPathsConfig.AUTH, tags=["auth"])
api_router.include_router(login_router, prefix=URLPathsConfig.LOGIN, tags=["login"])