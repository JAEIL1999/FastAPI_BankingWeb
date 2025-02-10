from fastapi import APIRouter, Depends
from app.services.account import transfer_funds
from app.schemas.account import Transfer
from app.dependencies import get_db
from sqlmodel import Session

router = APIRouter()

@router.post("/transfer") # 계좌 이체 처리
async def transfer(transfer_detail: Transfer, db: Session=Depends(get_db)):
    # 송금 요청을 서비스로 전달
    result = transfer_funds(transfer_detail, db)
    return result

@router.delete("/account/{account_id}")
async def delete_account(account_id: int):
    pass  # 계좌 삭제 처리

@router.post("/account")
async def add_account():
    pass  # 계좌 추가 개설 처리
