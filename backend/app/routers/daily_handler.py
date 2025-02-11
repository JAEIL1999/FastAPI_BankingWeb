from fastapi import APIRouter, Depends, HTTPException
from app.schemas.daily_schemas import *
from app.dependencies import get_db
from sqlmodel import Session, select
from app.models.models import Account, Transactions, User

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

# 로그인 성공 후 이름 띄우기
@router.get("/users/{user_id}/home")
def get_name(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.login_id == user_id).first()

     # 사용자 없으면 404 오류 발생
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 사용자 이름 반환
    return {"name": user.name}