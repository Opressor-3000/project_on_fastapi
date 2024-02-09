from datetime import datetime


from typing import Optional


from pydantic import BaseModel
from admin.schemes import PermissionId
from chat.schemes.chatuser import ChatUserId


class BaseMessage(BaseModel):
   chatuser_id: ChatUserId
   text: str
   

class MessageID(BaseMessage):
   id: int


class BanMessage(BaseMessage):
   creater_id: PermissionId
   delete:bool
   deleted_at: datetime