from fastapi import HTTPException
from app.models.model import Account
from sqlmodel import Session, select

class AccountService:
    def get_account(self, db:Session, account_id: int) -> Account:
        account = db.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Post not found")
        return account
    
    def get_accounts(self, db: Session, page: int=1,
                      limit: int=10) -> list[Account]:
        nOffset = (page-1) * limit
        accounts = db.exec(
            select(Account).offset(nOffset).limit(limit)
        ).all()
        return accounts
    
    def create_account(self, db: Session, account: Account) -> Account:
        db.add(account)
        db.commit()
        db.refresh(account)
        return account
    
    def update_account(self, db: Session, account_id: int, money: int, account: Account) -> Account:
        oldAccount = self.get_account(db, account_id)
        accountData = account.model_dump(exclude_unset=True)
        oldAccount.sqlmodel_update(accountData)
        db.add(oldAccount)
        db.commit()
        db.refresh(oldAccount)
        return oldAccount
    
    def delete_account(self, db: Session, account_id: int):
        account = self.get_account(db, account_id)
        db.delete(account)
        db.commit()



def create_account(account_data):
    pass  # 계좌 추가 생성 로직

def transfer_funds(transfer_data):
    pass  # 계좌 이체 처리 로직

def delete_account(account_id):
    pass  # 계좌 삭제 처리 로직



