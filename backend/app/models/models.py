from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional

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
    
    login_id:str = Field(index=True) #필수적인 요소인가?
    password:str = Field(default = None) #password : hashed value
    
    #accounts: List[str] | None = Field(default_factory=list)
    balance: int = 0 # account total money
    
    created_at: int | None = Field(index=True)
    access_token : str | None = None

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int
    account_id: int
    balance: int

class Transactions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sender: int = Field(foreign_key="account.owner_id")
    receiver: int = Field(foreign_key="account.owner_id")
    amount: float
    timestamp: datetime = Field(default=datetime.now(timezone.utc))
    
class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    account_id: int