from fastapi import APIRouter, Depends
from app.services.account_service import AccountService
from app.schemas.account_schemas import Transfer
from app.dependencies import get_db
from sqlmodel import Session
from app.schemas.account_schemas import RespAccounts, Account, AccountCreate

router = APIRouter()

# 계좌 이체
@router.post("/transfer")
def transfer(transfer_detail: Transfer, db: Session=Depends(get_db)):
    # 송금 요청을 서비스로 전달
    result = AccountService.transfer_funds(transfer_detail, db)
    return result

# 계좌 목록
@router.get("/users/account")
def get_accounts(page: int=1, limit: int=10,
                 session=Depends(get_db),
                 service: AccountService = Depends()) -> RespAccounts:
    if page < 1:
        page = 1
    if limit < 1 or limit > 10:
        limit = 10
    accounts_data = service.get_accounts(session, page, limit)
    return RespAccounts(
        accounts=accounts_data,
        page = page,
        limit = limit
    )

# 계좌 생성 
@router.post("/users/account", status_code=201)
def create_account(account: Account,
                   session = Depends(get_db),
                   service: AccountService = Depends()):                    
    new_account = Account(**account.model_dump())
    service.create_account(session, account)
    return new_account

# 계좌 삭제 
@router.delete("/{account_id}")
def delete_account(account_id: int,
                   session=Depends(get_db),
                   service: AccountService = Depends()):
    service.delete_account(session, account_id)
    return {}