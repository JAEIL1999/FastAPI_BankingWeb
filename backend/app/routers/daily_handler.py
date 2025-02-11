from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.dependencies import get_db
from app.models.models import Account, Transactions, User
from datetime import datetime, date

router = APIRouter()

@router.get("/users/{user_id}/transactions/monthly/{year}/{month}")
def get_monthly_transactions(user_id: str, year: int, month: int, db: Session = Depends(get_db)):
    # 유저의 모든 account_id 가져오기
    accounts = db.query(Account.account_id).filter(Account.owner_id == user_id).all()
    account_ids = [account_id for (account_id,) in accounts]

    if not account_ids:
        return {}

    # 해당 월의 첫날과 마지막 날 계산
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    # 해당 월의 거래 내역 가져오기
    transactions = db.query(Transactions).filter(
        Transactions.timestamp >= start_date,
        Transactions.timestamp < end_date,
        (Transactions.sender.in_(account_ids) | Transactions.receiver.in_(account_ids))
    ).all()

    # 날짜별로 입출금 정리
    daily_totals = {}

    for tx in transactions:
        day = tx.timestamp.day
        if day not in daily_totals:
            daily_totals[day] = {"out": 0, "in": 0}

        if tx.sender in account_ids:
            daily_totals[day]["out"] += tx.amount
        if tx.receiver in account_ids:
            daily_totals[day]["in"] += tx.amount

    return daily_totals

# 로그인 성공 후 이름 띄우기
@router.get("/users/{user_id}/home")
def get_name(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.login_id == user_id).first()

     # 사용자 없으면 404 오류 발생
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 사용자 이름 반환
    return {"name": user.name}