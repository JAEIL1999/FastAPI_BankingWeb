from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int
    account_id: int
    balance: int

class AccountCreate(BaseModel):
    owner_id: int
    account_id: int
    balance: int

class RespAccounts(BaseModel):
    accounts: List[Account]
    page: int
    limit: int

class UserReq(BaseModel):
    id: int
    user_id: int
    name: str

class UserResp(BaseModel):
    pass

class AccountReq(BaseModel):
    owner_id: int
    account_id: int
    balance: int = 0

class AccountResp(BaseModel):
    pass
