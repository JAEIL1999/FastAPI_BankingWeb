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

# TODO: 계좌 생성, 계좌 삭제는 프론트엔드 연결작업만 처리하면 된다.
# TODO: POST, DELETE를 어떻게 프론트엔드에 연결할지 고민해보기
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
@router.get("/user/{jwt_token}")
def transfer_log(jwt_token: str,
                 session=Depends(get_db),
                 service: AccountService = Depends(),
                 decording: JWTTool = Depends()) -> Transfer_log:
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]

    logs = AccountService.transfer_logs(session, user_id)
    return logs
