from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def signup():
    pass  # 회원가입 처리

@router.post("/login")
async def login():
    pass  # 로그인 처리

@router.post("/logout")
async def logout():
    pass  # 로그아웃 처리

@router.post("/recover")
async def recover():
    pass  # 비밀번호 찾기 처리
