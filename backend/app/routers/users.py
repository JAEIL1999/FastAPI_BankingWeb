#SERVICE import -> 해당 클래스 함수 활용
#SERVICE 함수를 사용하고, 예외처리는 ROUTER에서 수행

from fastapi import APIRouter, Depends, HTTPException
from app.models.models import UserSigninReq, UserSignupReq, UserRecoverReq
from app.services.users import UserService
from app.dependencies import get_db, JWTTool

router = APIRouter()
# 꼭 비동기 처리를 해야 하는가?
@router.post("/signup")
def signup(req: UserSignupReq, #jwt Token 부분 추가해야 함
                 db=Depends(get_db),userService:UserService=Depends(),
                 jwtTool:JWTTool=Depends()):
    user = userService.signup_user(db,req.login_id,req.password,req.name,jwtTool)
    
    if not user:
        raise HTTPException(status_code=400,
                            detail="SOMETHING WRONG!!") 
    return user
    # 회원가입 처리

@router.post("/login")
def login(req:UserSigninReq, #jwt Token 부분 추가해야 함
                db=Depends(get_db),userService:UserService=Depends(),
                jwtTool:JWTTool=Depends()):
    user = userService.login_user(db,req.login_id,req.password)
    if not user:
        raise HTTPException(status_code=401,
                            detail="FAILED")
    payload = {
        "user_id": req.login_id
    }
    user.access_token = jwtTool.create_token(payload=payload)
    
    return user
    # 로그인 처리

@router.post("/logout")
def logout():
    pass  # 로그아웃 처리

@router.post("/recover")
def recover(req:UserRecoverReq,
                  db=Depends(get_db), userService:UserService=Depends(),
                  jwtTool:JWTTool=Depends()):
    user = userService.recover_password(db, req.login_id, req.name,jwtTool)
    if not user:
        raise HTTPException(status_code=404,
                            detail="NOT FOUND")
    
    return user
    pass  # 비밀번호 찾기 처리
