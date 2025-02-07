from fastapi import APIRouter

router = APIRouter()

@router.post("/favorites")
async def add_favorite():
    pass  # 즐겨찾기 추가 처리

@router.delete("/favorites/{favorite_id}")
async def delete_favorite(favorite_id: int):
    pass  # 즐겨찾기 삭제 처리
