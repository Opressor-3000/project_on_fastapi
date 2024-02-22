from typing import Annotated, List


from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession


from account.schemes.user import UserCreate
from account.crud import create_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/account_auth/")
async def main_auth():
    pass


# @router.post('/add_cookie/', response_model=None, status_code=status.HTTP_201_CREATED)
# async def cookie_auth(session: AsyncSession, user_data: UserCreate):
#     await create_user(session=session, user=user_data)
#     return RedirectResponse(url='api/v1/chat/', status_code=status.HTTP_302_FOUND)


@router.get("/")  # страница для отправки сообщения и регистрации
async def create_user(
    token: str | None = None, cookie: str | None = None, username=None
):
    """
    возвращает all chats user order_by(created_at)
     all message chats order_by(created_at) если есть:
        1. Bearer token -> account with DB, а иначе
        2. user в DB с таким cookie, а иначе
        3. create cookie and create new User and redirect
        4. для отправки сообщения просит ввести имя
    """
    pass


async def validation_auth_jwt(phone: int, password: bytes):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="incorrectly entered phone number and/or password",
    )
    return unauthed_exc


async def validation_phone(account: dict):
    phone: str = account.phone
    if phone.isdigit:
        return True
    else:
        return "phone number does not consist only of numbers"


@router.post("/jwt_logig/")
async def auth_account_jwt():
    pass


@router.post("/jwt_singin/")
async def account_singin():
    pass
