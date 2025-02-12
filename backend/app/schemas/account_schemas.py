from pydantic import BaseModel
from typing import List
from app.models.models import Account, Transactions

class Transfer(BaseModel):
    sender: int
    receiver: int
    amount: float

class Transfer_log(BaseModel):
    transfer_list: list[Transactions]
    
class UserAccounts(BaseModel):
    accounts: List[Account]
