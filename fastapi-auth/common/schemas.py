from pydantic import BaseModel
#from typing import Optional
from typing import Union



class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    #username: str | None = None
    #username: Optional(str) = None
    username: Union[str, None] = None
