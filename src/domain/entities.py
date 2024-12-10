from uuid import UUID, uuid4
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


# TODO: maybe add BaseOAuthUserByPhone and BaseOAuthUserByEmail
class BaseOAuthUser(BaseModel):
    """
        Base OAuth User Model
    """
    id: str | PydanticObjectId
    email: EmailStr | None
    verified_email: bool
    name: str
    picture: str | None
    locale: str
    phone_number: str | None


# TODO: find immutable atr fore every provider
class GoogleUser(BaseOAuthUser):
    """
        Google User Model
    """
    pass 

class VKUser(BaseOAuthUser):
    """
        VK User Model
    """
    pass

class YandexUser(BaseOAuthUser):
    """
        Yandex User Model
    """
    pass

class User(BaseModel):
    """
        User Model
    """
    id: str | PydanticObjectId  # ? is it good to bind domani area to  MongoDB-specific types ?
    # TODO: add filds about user
    login: str 
    email: EmailStr | None = None
    phone: PhoneNumber | None = None
    password: str | None = None

    google_acc: GoogleUser | None = None
    vk_acc: VKUser | None = None
    yandex_acc: YandexUser | None = None
    # TOOD: add "ByPhoneAcc"
