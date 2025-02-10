from app.models.account import Account, Transaction
from app.schemas.account import Transfer
from sqlmodel import Session
from app.dependencies import get_db

def create_account(account_data):
    pass  # 계좌 추가 생성 로직

def transfer_funds(transfer_details: Transfer, db: Session): # 계좌 이체 처리 로직
    # 계좌 정보 조회
    sender = db.query(Account).filter(Account.id == transfer_details.sender).first()
    receiver = db.query(Account).filter(Account.id == transfer_details.receiver).first()
    
    # 계좌가 존재하지 않으면 오류 처리
    if not sender or not receiver:
        return {"error": "존재하지 않는 계좌입니다."}
    
    # 계좌 잔액 확인
    if sender.banlance < transfer_details['amount']:
        return {"error": "잔액이 부족합니다."}
    
    # 송금 처리
    sender.balance -= transfer_details['amount']
    receiver.balance += transfer_details['amount']    
    
    # 거래 내역에 추가
    transaction = Transaction(
        sender_id=transfer_details['sender_id'], 
        receiver_id=transfer_details['receiver_id'],
        amount=transfer_details['amount'],) 
    # timestamp는 자동으로 현재 시간이 기록됨 - models/transaction.py에서 처리

    db.add(transaction)
    db.commit()
    
    return {"status": "Transfer successful"}

def delete_account(account_id):
    pass  # 계좌 삭제 처리 로직
