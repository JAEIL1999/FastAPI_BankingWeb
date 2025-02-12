from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.dependencies import get_db, JWTTool
from app.models.models import Favorite

router = APIRouter()

# 사용자별 즐겨찾기 목록 조회
@router.get('/users/favorites/{user_id}')
async def get_favorite(user_id: str, db: Session = Depends(get_db)):
    # user_id에 해당하는 즐겨찾기 목록 조회
    favorites = db.exec(select(Favorite).where(Favorite.user_id == user_id)).all()
    return favorites

# 즐겨찾기 추가
@router.post("/favorites/{user_id}")
async def add_favorite(user_id: str, account_id: int, db: Session = Depends(get_db)):
    # 즐겨찾기 추가
    favorite = Favorite(user_id=user_id, account_id=account_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

# 즐겨찾기 삭제
@router.delete("/favorites/{user_id}/{account_id}")
async def delete_favorite(user_id: str, account_id: int, db: Session = Depends(get_db)):  
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
