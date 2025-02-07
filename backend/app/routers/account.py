from fastapi import APIRouter

router = APIRouter()

@router.post("/transfer")
async def transfer():
    pass  # 계좌 이체 처리

@router.delete("/account/{account_id}")
async def delete_account(account_id: int):
    pass  # 계좌 삭제 처리

@router.post("/account")
async def add_account():
    pass  # 계좌 추가 개설 처리
