from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.dependencies import get_db
from app.models.models import Favorite

router = APIRouter()

# 사용자별 즐겨찾기 목록 조회 
@router.get('/users/{users_id}/favorites')
async def get_favorite(user_id: int, db: Session=Depends(get_db)):
    favorites = db.exec(select(Favorite).where(Favorite.user_id == user_id)).all()
    return favorites

# 즐겨찾기 추가
@router.post("/favorites")
async def add_favorite(user_id: int, account_id: int, db: Session=Depends(get_db)):
    favorite = Favorite(user_id=user_id, account_id= account_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

# 즐겨찾기 삭제 
@router.delete("/users/{user_id}/favorites/{account_id}")
async def delete_favorite(user_id: int, account_id: int, db: Session=Depends(get_db)):
    favorite = db.exec(
        select(Favorite).where(
            Favorite.user_id == user_id,
            Favorite.account_id == account_id
        )
    ).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    
    db.delete(favorite)
    db.commit()
    return {"message":"즐겨찾기 삭제 완료"}
