from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from .schemes import BasicCookieAuth
from account.models import User
from account.schemes import UserCookie, UserScheme
from account.crud import create_user
from main import session_id_generate, COOKIE_SESSION_ID
from core.models import db_connect


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/account_auth/')
async def set_auth(phone):
    pass


@router.get('/comfirmation_phone/')
async def get_phone():
    pass


@router.post('/comfirmation_phone/')
async def comfirmation_phone():
    pass


@router.post('/add_cookie/', response_model=User, status_code=status.HTTP_201_CREATED)
async def cookie_auth(session: AsyncSession, user_data: UserScheme):
    await create_user(session=session, user=user_data)
    return RedirectResponse(url='api/v1/chat', status_code=status.HTTP_302_FOUND)


@router.post('/autorization/')
async def autorization():
    pass


