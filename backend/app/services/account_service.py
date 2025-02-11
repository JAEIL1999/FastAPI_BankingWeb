from app.models.models import Account, Transactions
from app.schemas.account_schemas import Transfer, Account
from sqlmodel import Session, select
from fastapi import HTTPException

class AccountService:
    # 특정 계좌 확인(계좌 id 기준)
    def get_account(self, db:Session, account_id: int) -> Account:
        account = db.query(Account).filter(Account.account_id == account_id).first()
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return account
    
    # 계좌 목록 조회
    def get_accounts(self, db: Session, page: int=1,
                      limit: int=10) -> list[Account]:
        nOffset = (page-1) * limit
        accounts = db.exec(
            select(Account).offset(nOffset).limit(limit)
        ).all()
        return accounts
    
    # 계좌 생성
    def create_account(self, db: Session, account: Account) -> Account:
        db.add(account)
        db.commit()
        db.refresh(account)
        return account
    
    # 계좌 삭제
    def delete_account(self, db: Session, account_id: int):
        account = self.get_account(db, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Post not found")
        db.delete(account)
        db.commit()

    def transfer_funds(transfer_details: Transfer, db: Session):
        # 계좌 정보 조회
        sender = db.query(Account).filter(Account.owner_id == transfer_details.sender).first()
        receiver = db.query(Account).filter(Account.owner_id == transfer_details.receiver).first()
        
        # 계좌가 존재하지 않으면 오류 처리
        if not sender or not receiver:
            return {"error": "존재하지 않는 계좌입니다."}
        
        # 계좌 잔액 확인
        if sender.balance < transfer_details.amount:
            return {"error": "잔액이 부족합니다."}
        
        # 송금 처리
        sender.balance -= transfer_details.amount
        receiver.balance += transfer_details.amount    
        
        # 거래 내역에 추가
        transaction = Transactions(
        sender=transfer_details.sender, 
        receiver=transfer_details.receiver,
        amount=transfer_details.amount
        )
        # timestamp는 자동으로 현재 시간이 기록됨 - models/transaction.py에서 처리

        db.add(transaction)
        db.commit()
        db.refresh(sender)
        db.refresh(receiver)
        db.refresh(transaction)
        
        return {"status": "Transfer successful"}
