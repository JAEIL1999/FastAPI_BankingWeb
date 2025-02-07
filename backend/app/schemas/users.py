from pydantic import BaseModel

class UserSignup(BaseModel):
    name: str
    user_id: str
    password: str
    

class UserLogin(BaseModel):
    user_id: str
    password: str

# 추가사항
class PasswordRecovery(BaseModel):
    email: str
