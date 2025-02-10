from pydantic import BaseModel

class Account(BaseModel):
    account_id: int
    user_id: int
    balance: float

class Transfer(BaseModel):
    sender: int
    receiver: int
    amount: float