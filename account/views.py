from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

# from .schemes.user import UserCreate, UserID

router = APIRouter(prefix="/account", tags=["Account"])

"""
    router for user 

    #######    POST     #######

"""


#         POST


@router.post("/registration/")  #
async def create_account(create_account_scheme):
    pass


@router.post("/comfirmation_phone/")
async def comfirmation_phone():
    """
    run after post registration
    """
    pass


@router.post("/support/")
async def create_issue():
    pass


#         PATCH


@router.patch("/{uuid}/{feedback_id}/")
async def patch_feedback():
    """
    edit account feedback
    """
    pass


@router.patch("/edit_account/{uuid}/")  # after click edit account
async def account_active():
    """
    возвращает форму с заполненными полями для редактирования если:
        1. Account
    поля:
    """
    pass


#            GET       


@router.get("/result_comfirmation_phone/")
async def get_phone():
    """
    return answer post comfirmation phone
        True or False
    """
    pass


@router.get("/{uuid}/")
async def get_account():
    """
    return account if is auth

        1. id
        2. First Name
        3. Last Name
        4. avatar
        5. chatsuser_list(user.account = account)(get_chat_list, chatuser=user_id)
        6. accesses_list
        7. sertificates(doctor.account=account)(doctor.is_active-true)

    """
    pass


@router.get("/statistic/{user_id}/")
async def get_user_statistic_data():
    '''
        user page:
            username, avatar, gender (click get_user_data)
            1. count(chat doctor)
            2. list(chat doctor)
                            yes/no(chat doctor without feedback)
            3. count(chat without rating)
            4. count(chat doctor without feedback)
            5. list(feedback)count(feedback)
    '''
    pass


@router.get("/{uuid}/my_doctors/")
async def get_doctors():
    """
    return doctor with which chats
        1.[ user > chat > doctor 
                                > account 
                                        > first name 
                                        > last name
                                > speciality 
                                        > title
        ]
    """
    pass


@router.get('/chats/')
async def get_account_all_chat():
    '''
        list[user.account = account] 
                                    > list[chat]
    '''
    pass


@router.get('/{user_cookie}/')
async def get_user_data():
    '''
        username
        avatar (click for select/change)
        gender(click for select)
    '''
    pass


@router.get("/{uuid}/{feedback_id}/")
async def get_feedback():
    pass


@router.get("/{uuid}/feedbacks/")
async def get_feedbacks():
    return
