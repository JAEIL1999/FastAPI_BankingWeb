from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str

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