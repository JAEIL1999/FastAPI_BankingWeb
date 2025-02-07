from pydantic import BaseModel

class Account(BaseModel):
    account_id: int
    user_id: int
    balance: float


class Transfer(BaseModel):
    from_account: int
    to_account: int
    amount: float
    date: int