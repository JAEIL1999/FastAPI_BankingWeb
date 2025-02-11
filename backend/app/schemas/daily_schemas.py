from pydantic import BaseModel
from typing import Optional

class Dailyreq(BaseModel):
	year_month: str #YYYY-MM
	trs_type: str #in/out
	
class Transaction(BaseModel):
	date: str 
	amount: int
	account: int
	
class Dailyresp(BaseModel):
	transactions: list[Transaction]
	err_msg: Optional[str] = None
