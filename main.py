from fastapi import FastAPI, Depends
from app.routers import account_handler
from app.dependencies import ( create_user_db_and_tables, 
                              get_user_db_session, create_account_db_and_tables
                              )
from sqlmodel import Session
from app.models.model import *


app = FastAPI()
create_user_db_and_tables()
create_account_db_and_tables()

@app.post("/user")
def create_user(user: User,
                   session = Depends(get_user_db_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user



# 홈 화면 라우터 포함
app.include_router(account_handler.router)
