from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.middleware.sessions import SessionMiddleware

from src.configs.settings import get_settings
from src.configs.urls import URLPathsConfig
from src.presentation.routers import api_router

app = FastAPI(
    root_path=URLPathsConfig.API_V1_STR,
    title="BigsAuto API",
    version="0.1.0",
    docs_url=URLPathsConfig.DOCS,
    openapi_url=URLPathsConfig.OPENAPI,
)

app.add_middleware(
    SessionMiddleware,
    secret_key=get_settings().SECRET_KEY,
    # http_only=True, # TODO: set to True in production
    # store=RedisSession(redis)  # TODO: add Reddis storage 
    # for JWT access token
)
app.add_middleware(
    CORSMiddleware,  # TODO: add real middlevare
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=api_router)

@app.get(
        path=URLPathsConfig.HOMEPAGE,
        response_class=RedirectResponse,
        status_code=status.HTTP_303_SEE_OTHER
)
async def root():
    return RedirectResponse(
        status_code=status.HTTP_303_SEE_OTHER,
        url=URLPathsConfig.DOCS
    )