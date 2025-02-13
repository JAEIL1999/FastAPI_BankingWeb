from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlmodel import Session, select
from app.dependencies import get_db, JWTTool
from app.models.models import Favorite

router = APIRouter()

# 사용자별 즐겨찾기 목록 조회
@router.get('/users/favorites')
async def get_favorite(jwt_token: str, db: Session = Depends(get_db), decording: JWTTool = Depends()):
    # JWT 토큰 디코딩
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]
    
    # user_id에 해당하는 즐겨찾기 목록 조회
    favorites = db.exec(select(Favorite).where(Favorite.user_id == user_id)).all()
    return favorites

class FavoriteCreateRequest(BaseModel):
    account_id: int

# 즐겨찾기 추가
@router.post("/users/favorites")
async def add_favorite(
    request: FavoriteCreateRequest,  
    jwt_token: str = Header(...),  # 헤더에서 토큰 받기
    db: Session = Depends(get_db), 
    decording: JWTTool = Depends()
):
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]

    favorite = Favorite(user_id=user_id, account_id=request.account_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

# 즐겨찾기 삭제
@router.delete("/favorites/{account_id}")
async def delete_favorite(jwt_token: str, account_id: int, db: Session = Depends(get_db), decording: JWTTool = Depends()):
    # JWT 토큰 디코딩
    payload = decording.decode_token(jwt_token)
    user_id = payload["user_id"]
    
    # 즐겨찾기 항목 조회
    favorite = db.exec(
        select(Favorite).where(
            Favorite.user_id == user_id,
            Favorite.account_id == account_id
        )
    ).first()
    
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    
    # 즐겨찾기 삭제
    db.delete(favorite)
    db.commit()
    return {"message": "즐겨찾기 삭제 완료"}