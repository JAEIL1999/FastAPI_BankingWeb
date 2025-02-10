from fastapi import APIRouter

router = APIRouter()

@router.get('/users/{users_id}/favorites')
async def get_favorite():
    pass # 사용자별 즐겨찾기 목록 불러오기

@router.post("/favorites")
async def add_favorite():
    pass  # 즐겨찾기 추가 처리

@router.delete("/favorites/{favorite_id}")
async def delete_favorite(favorite_id: int):
    pass  # 즐겨찾기 삭제 처리
