from pydantic import BaseModel,validator, datetime_parse
import re
from enum import Enum
from datetime import datetime,date

class StatusEnum(str, Enum):
    send = 'send'
    done = 'done'

class UserOut(BaseModel):
    email:str
    name:str

    class config():
        from_attributes = True
    
    
class Auth(UserOut):
    password: str

    class config():
        from_attributes = True

class UserIn(BaseModel):
    email:str
    name:str
    created_at:  date | None = None 
    password: str
    class config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

    class config():
        from_attributes = True

class ResetPassword(BaseModel):
    id: int | None = None
    user_id: Auth
    status: StatusEnum
    code: str

    class config():
        from_attributes = True


class LinkShortIn(BaseModel):
    link_long: str
    short_link: str

    class config():
        from_attributes = True

class LinkShortOut(BaseModel):
    link_long: str

    class config():
        from_attributes = True