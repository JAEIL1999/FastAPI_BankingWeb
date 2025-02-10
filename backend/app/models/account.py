from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

class Account(SQLModel, table=True):
    __tablename__ = 'accounts'

    id: int = Field(default=None, primary_key=True)
    account_number: str = Field(index=True, sa_column_kwargs={"unique": True})
    balance: float = Field(default=0.0)

# 송금 내역 모델
class Transaction(SQLModel, table=True):
    __tablename__ = 'transactions'

    id: int = Field(default=None, primary_key=True)
    sender_id: int = Field(foreign_key="accounts.id")
    receiver_id: int = Field(foreign_key="accounts.id")
    amount: float
    timestamp: datetime = Field(default=datetime.now(timezone.utc))