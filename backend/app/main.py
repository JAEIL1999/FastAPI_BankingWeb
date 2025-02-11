from fastapi import FastAPI
from app.routers import users, account_handler, favorites_handler, home, daily_handler
from app.dependencies import create_db
from app.models.models import *
from fastapi.middleware.cors import CORSMiddleware

create_db()
app = FastAPI()

# 홈 화면 라우터 포함
app.include_router(home.router)

# 다른 기능별 라우터들 포함
app.include_router(users.router)
app.include_router(account_handler.router)
app.include_router(favorites_handler.router)
app.include_router(daily_handler.router)

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 접근 허용 (보안이 필요한 경우 특정 도메인으로 제한)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)