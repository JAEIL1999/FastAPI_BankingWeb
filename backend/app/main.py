from fastapi import FastAPI, Depends
from app.routers import users, account_handler, favorites_handler, home, daily_handler
from app.dependencies import create_db, get_db
from app.models.models import *

create_db()
app = FastAPI()

# 홈 화면 라우터 포함
app.include_router(home.router)

# 다른 기능별 라우터들 포함
app.include_router(users.router)
app.include_router(account_handler.router)
app.include_router(favorites_handler.router)
app.include_router(daily_handler.router)
