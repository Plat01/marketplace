from dataclasses import dataclass


@dataclass(frozen=True)
class URLPathsConfig:
    API_V1_STR: str = '/api/v1'
    HOMEPAGE: str = '/'

    DOCS: str = '/docs'
    OPENAPI: str = '/openapi.json'

    AUTH: str = "/auth"
    # GOOGLE 
    GOOGLE: str = f"/google"
    GOOGLE_AUTH_CALLBACK: str = f"{GOOGLE}/callback"

    # YANDEX
    YANDEX: str = f"/yandex"
    YANDEX_AUTH_CALLBACK: str = f"{YANDEX}/callback"

    # VK
    VK: str = f"/vk"
    VK_AUTH_CALLBACK: str = f"{VK}/callback"

    # LOGIN
    LOGIN: str = "/login"
    GOOGLE_LOGIN: str = f"{GOOGLE}"
    YANDEX_LOGIN: str = f"{YANDEX}"
    VK_LOGIN: str = f"{VK}"
    
    LOGOUT: str = "/logout"
