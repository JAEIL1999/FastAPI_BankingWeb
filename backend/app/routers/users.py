from fastapi import APIRouter

router = APIRouter()

@router.get("/users/signup")
def signup():
    return {"message": "Signup Page"}

@router.get("/users/login")
def login():
    return {"message": "Login Page"}
