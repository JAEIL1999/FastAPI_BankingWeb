from fastapi import APIRouter, Depends
from app.schemas.daily_schemas import *
from app.dependencies import get_db
from sqlmodel import Session, select
from app.models.models import Account, Transactions

router = APIRouter()

# owner_id -> account_id -> timestamp, amount
@router.get("/users/{user_id}/transactions/daily")
def get_transactions(user_id: int,
                    db: Session = Depends(get_db)): # -> Dailyresp
    
    # user_id에 해당하는 모든 account_id 가져오기
    accounts = db.query(Account.account_id).filter(Account.owner_id == user_id).all()
    account_ids = [account_id for (account_id,) in accounts]

    # 계정이 없으면 빈 리스트 반환
    if not account_ids:
        return [] 
    
    trans_out = db.query(Transactions).filter(Transactions.sender.in_(account_ids)).all()
    trans_in = db.query(Transactions).filter(Transactions.receiver.in_(account_ids)).all()
    return {
        "out" : trans_out,
        "in" : trans_in
    }