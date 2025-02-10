from fastapi import FastAPI, Depends
from app.routers import users, account_handler, favorites, home
from app.dependencies import create_db, get_db
from app.models.account_model import *

create_db()
app = FastAPI()

@app.post("/user")
def create_user(user: User,
                   session = Depends(get_db)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# 홈 화면 라우터 포함
app.include_router(home.router)

# 다른 기능별 라우터들 포함
app.include_router(users.router)
app.include_router(account_handler.router)
app.include_router(favorites.router)
