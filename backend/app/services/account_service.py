from app.models.models import Account, Transactions
from app.schemas.account_schemas import Transfer, Account, Transfer_log
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
    def get_accounts(self, db: Session, user_id: int) -> list[Account]:
        accounts = []
        offset = 0
        batch_size = 10

        while True:
            account_arr = db.query(Account).filter(Account.owner_id == user_id).offset(offset).limit(batch_size).all()
            if not account_arr:
                break

            accounts.extend(account_arr)
            offset += batch_size

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
        sender = db.query(Account).filter(Account.account_id == transfer_details.sender).first()
        receiver = db.query(Account).filter(Account.account_id == transfer_details.receiver).first()
        
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
    
    # 계좌이체 내역
    def transfer_logs(self, db: Session, user_id: int) -> Transfer_log:
        user_logs = Transfer_log()
        offset = 0
        batch_size = 10

        while True:
            logs = db.query(Transactions).filter(Transactions.sender == user_id).offset(offset).limit(batch_size).all()

            if not logs:
                break
            user_logs.transfer_list.extend(logs)  # 반환된 로그를 리스트에 추가

            offset += batch_size
            
        return user_logs

