from fastapi import APIRouter

router = APIRouter()

@router.get("/users/account")
def account():
    return {"message": "Account Page"}

@router.get("/users/account/favorites")
def favorites():
    return {"message": "Favorites Page"}

@router.get("/users/account/transfer")
def transfer():
    return {"message": "Transfer Page"}

@router.get("/users/account/transaction")
def transaction():
    return {"message": "Transaction Page"}
