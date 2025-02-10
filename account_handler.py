from app.services.account_service import AccountService
from app.dependencies import get_account_db_session
from fastapi import Depends, APIRouter
from app.models.model import RespAccounts, Account, AccountCreate

router = APIRouter()

@router.get("/users/account")
def get_accounts(page: int=1, limit: int=10,
                 session=Depends(get_account_db_session),
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

@router.post("/users/account", status_code=201)
def create_account(account: Account,
                   session = Depends(get_account_db_session),
                   service: AccountService = Depends()):                    
    new_account = Account(**account.model_dump())
    service.create_account(session, account)
    return new_account

@router.delete("/{account_id}")
def delete_account(account_id: int,
                   session=Depends(get_account_db_session),
                   service: AccountService = Depends()):
    service.delete_account(session, account_id)
    return {}