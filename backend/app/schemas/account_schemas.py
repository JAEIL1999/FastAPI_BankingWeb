from pydantic import BaseModel
from typing import List
from app.models.models import Account

class Transfer(BaseModel):
    sender: int
    receiver: int
    amount: float
    
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
