from fastapi import FastAPI
from app.routers import users, account

app = FastAPI()

app.include_router(users.router)
app.include_router(account.router)
