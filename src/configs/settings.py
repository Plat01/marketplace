from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    PROJECT_NAME: str = "BigsAuto"
    API_V1_STR: str = "/api/"
    SECRET_KEY: str

    # TODO: check if all of tins URL correct
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_CALLBACK_URL: str = "http://0.0.0.0:8000/api/v1/auth/google/callback"

    GOOGLE_AUTHORIZATION_ENDPOINT: str = "https://accounts.google.com/o/oauth2/v2/auth"
    GOOGLE_TOKEN_ENDPOINT: str = "https://oauth2.googleapis.com/token"
    GOOGLE_USERINFO_ENDPOINT : str = "https://www.googleapis.com/oauth2/v2/userinfo"

    YANDEX_CLIENT_ID: str
    YANDEX_CLIENT_SECRET: str
    YANDEX_REDIRECT_URI: str

    YANDEX_AUTHORIZATION_ENDPOINT: str = "https://oauth.yandex.ru/authorize"
    YANDEX_TOKEN_ENDPOINT: str = "https://oauth.yandex.ru/token"
    YANDEX_USERINFO_ENDPOINT : str = "https://login.yandex.ru/info"

    VK_CLIENT_ID: str
    VK_CLIENT_SECRET: str   
    VK_REDIRECT_URI: str

    VK_AUTHORIZATION_ENDPOINT: str = "https://oauth.vk.com/authorize"
    VK_TOKEN_ENDPOINT: str = "https://oauth.vk.com/access_token"
    VK_USERINFO_ENDPOINT : str = "https://api.vk.com/method/users.get"

    MONGO_URI: str
    MONGO_DB_NAME: str = "auth_service"

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
    

@lru_cache()
def get_settings():
    return Settings()  # TODO: make it DI?
