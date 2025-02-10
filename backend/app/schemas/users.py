from pydantic import BaseModel,Field
from sqlmodel import SQLModel
from typing import List

#다시 설정하는 유저 CLASS
class User(SQLModel, table=True):
    id:int|None = Field(defalut=None, primary_key=True) #user id
    name:str = Field(index=True) #user name
    password:str = Field(default = None, exclude = True) #password : hashed value
    accounts: List[str] = Field(default_factory=list)
    balance: int = 0 # account total money
    access_token : str | None = None
