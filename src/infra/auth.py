from authlib.integrations.starlette_client import OAuth

from src.configs.settings import get_settings


oauth = OAuth()

# TODO: add all from get_settings()
oauth.register(
    name='google',
    client_id=get_settings().GOOGLE_CLIENT_ID,
    client_secret=get_settings().GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

oauth.register(
    name='vk',
    client_id=get_settings().VK_CLIENT_ID,
    client_secret=get_settings().VK_CLIENT_SECRET,
    authorize_url='https://oauth.vk.com/authorize',
    access_token_url='https://oauth.vk.com/access_token',
    api_base_url='https://api.vk.com/method/',
    client_kwargs={'scope': 'email'}
)

oauth.register(
    name='yandex',
    client_id=get_settings().YANDEX_CLIENT_ID,
    client_secret=get_settings().YANDEX_CLIENT_SECRET,
    authorize_url='https://oauth.yandex.com/authorize',
    access_token_url='https://oauth.yandex.com/token',
    api_base_url='https://login.yandex.ru/info',
    client_kwargs={'scope': 'login:email login:info'}
)