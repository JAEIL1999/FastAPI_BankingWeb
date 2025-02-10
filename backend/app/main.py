from fastapi import FastAPI
from app.routers import users, account, home

app = FastAPI()

# 홈 화면 라우터 포함
app.include_router(home.router)

# 다른 기능별 라우터들 포함
app.include_router(users.router)
app.include_router(account.router)

