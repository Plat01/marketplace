from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from authlib.integrations.starlette_client import OAuthError

from src.configs.urls import URLPathsConfig 
from src.infra.auth import oauth


auth_router = APIRouter()

@auth_router.get(URLPathsConfig.GOOGLE)
async def google_auth(request: Request):
    """
    
    Args:
        request (Request): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    try:
        token = await oauth.google.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    user_info = token.get('userinfo')
    if user_info:
        request.session['user'] = dict(user_info)  # TODO: add to database
        return JSONResponse(content=user_info)
    raise HTTPException(status_code=400, detail="Could not fetch user info")

@auth_router.get(URLPathsConfig.GOOGLE_AUTH_CALLBACK, name="google_auth_callback")
async def google_auth_callback(request: Request):
    """
    Function gets responce like http://localhost:8000/api/v1/auth/google/callback?state=RK75rQqSUSl65l1rCaNeLCa3PsnhmN&code=4%2F0AeanS0bMin2Xu-jskj7UVz6rqsTeACRJ8S_Ua7uiB8FzsxI-mFZBlsX6WJOeZD9-KfkEFw&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=0&prompt=consent
    which can containn sencetive data and shudn't been seen by users frontend in production
    Args:
        param (str): _description_
        request (Request): _description_

    Raises:
        HTTPException: _description_
    """

    # TODO: create user (or get user by unic attribute). And return Token (not JWT without refresh and access tokens)
    try:
        # Exchange the authorization code for an access token
        token = await oauth.google.authorize_access_token(request) 
        # return JSONResponse(content=token)  # TODO: delete this 
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to authorize: {str(e)}")
    user_info = token.get("userinfo")
    if not user_info:
        # If userinfo is not present, use the access token to fetch user info from Google
        try:
            resp = await oauth.google.get('https://www.googleapis.com/oauth2/v3/userinfo', token=token)  # TODO: replace with constant
            user_info = resp.json()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to fetch user info: {str(e)}")


    # `user_info_response` contains all the user information returned by Google
    return JSONResponse(content=user_info)


@auth_router.get(URLPathsConfig.YANDEX_AUTH_CALLBACK, name="yandex_auth_callback")
async def yandex_auth_callback(request: Request):
    """

    Args:
        request (Request
    Raises:
        OAuthError: _description_
    
    Returns:
            _type_: _description_
    """
    try:
        token = await oauth.yandex.authorize_access_token(request)
    except OAuthError as e: # TOOD: replace to logic layer
        raise HTTPException(status_code=400, detail=str(e))

    userinfo = await oauth.yandex.get("https://login.yandex.ru/info", token=token)
    if not userinfo:
        raise HTTPException(status_code=400, detail="Could not fetch user info")
    
    return JSONResponse(content=userinfo.json())

@auth_router.get(URLPathsConfig.VK_AUTH_CALLBACK, name="vk_auth_callback")
async def vk_auth_callback(request: Request):
    try:
        from src.configs.settings import get_settings
        print(get_settings().VK_CLIENT_ID, get_settings().VK_CLIENT_SECRET)
        print(request.cookies)
        print(request.headers)
        try:
            rq = await request.body()
            print(rq)
        except Exception as e:
            print(e)
        finally:
            rq = await request.body()
        print(rq)
        token = await oauth.vk.authorize_access_token(request)
        print(token)
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return JSONResponse(content=token)
    userinfo = token.get('userinfo')  # ?
    if not userinfo:
        raise HTTPException(status_code=400, detail="Could not fetch user info")

    return JSONResponse(content=userinfo)


login_router = APIRouter()

@login_router.get(URLPathsConfig.GOOGLE_LOGIN)
async def google_login(request: Request):
    redirect_uri = request.url_for(google_auth_callback.__name__)
    try:
        response = await oauth.google.authorize_redirect(request, redirect_uri)
        print(response)
        return response
    except Exception as e:  # TODO: add oAuthException 
        raise HTTPException(status_code=400, detail=str(e))
    
@login_router.get(URLPathsConfig.YANDEX_LOGIN)
async def yandex_login(request: Request):
    redirect_uri = request.url_for(yandex_auth_callback.__name__)
    try:
        response = await oauth.yandex.authorize_redirect(request, 'https://test.bigsauto.ru/api/v1/auth/yandex/callback')
        return response
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@login_router.get(URLPathsConfig.VK_LOGIN)
async def vk_login(request: Request):
    redirect_uri = request.url_for(vk_auth_callback.__name__)
    print(redirect_uri)
    try:
        response = await oauth.vk.authorize_redirect(request, "https://test.bigsauto.ru/api/v1/auth/vk/callback")
        return response
    except OAuthError as e:
        raise HTTPException