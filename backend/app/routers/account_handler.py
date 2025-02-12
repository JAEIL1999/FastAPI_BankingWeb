from fastapi import APIRouter, Depends
from app.services.account_service import AccountService
from app.schemas.account_schemas import Transfer, Account, UserAccounts, Transfer_log
from app.dependencies import get_db, JWTTool
from sqlmodel import Session

router = APIRouter()

# 계좌 이체
@router.post("/transfer")
def transfer(transfer_detail: Transfer, db: Session=Depends(get_db)):
    # 송금 요청을 서비스로 전달
    result = AccountService.transfer_funds(transfer_detail, db)
    return result

# 계좌 목록
@router.get("/users/account/{jwt_token}")
def get_accounts(jwt_token: str,
                 session=Depends(get_db),
                 service: AccountService = Depends(),
                 decording: JWTTool = Depends()) -> UserAccounts:
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]
    accounts_data = service.get_accounts(session, user_id)
    return UserAccounts(accounts=accounts_data)


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

# 송금 내역
# 인당 1개의 계좌밖에 내역이 안나옴 -> 문제 해결 필요
@router.get("/user/{jwt_token}")
def transfer_log(jwt_token: str,
                 session=Depends(get_db),
                 service: AccountService = Depends(),
                 decording: JWTTool = Depends()) -> Transfer_log:
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]
    sender = session.query(Account).filter(Account.user_id == user_id).first()
    if sender is None:
        raise HTTPException(status_code=404, detail="Account not found")

    logs = service.transfer_logs(session, sender.account_id)
    return logs
