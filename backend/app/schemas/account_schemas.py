from pydantic import BaseModel
from typing import List
from app.models.models import Account

class Transfer(BaseModel):
    sender: int
    receiver: int
    amount: float

class Transfer_log(BaseModel):
    transfer_list: list[Transfer]
    
class UserAccounts(BaseModel):
    accounts: List[Account]
