from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import String
from sqlalchemy.sql.schema import Column

class UserSigninReq(BaseModel):
    login_id: str
    password: str

class UserSignupReq(BaseModel):
    login_id: str
    password: str 
    name: str
    
class UserRecoverReq(BaseModel):
    login_id: str
    name: str
    
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True) #user id
    name:str = Field(index=True) #user name
    
    # login_id:str = Field(index=True) #필수적인 요소인가?
    login_id: str = Field(sa_column=Column("login_id", String, unique=True))
    password:str = Field(default = None) #password : hashed value
    
    #accounts: List[str] | None = Field(default_factory=list)
    balance: int = 0 # account total money
    
    created_at: int | None = Field(index=True)
    access_token : str | None = None

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    account_id: int
    balance: int

class Transactions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sender: int = Field(foreign_key="account.account_id") # 주는 계좌
    receiver: int = Field(foreign_key="account.account_id") # 받는 계좌
    amount: int
    timestamp: datetime = Field(default=datetime.now(timezone.utc))
    
class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    account_id: int
