#class 만들어서 CLASS_FUNCTION 만들기
#02.10 완성시키기
import bcrypt
import time
from sqlmodel import Session, select
from app.models.models import User
from jose import jwt
from app.dependencies import JWTTool, SECRET_KEY, ALGORITHM
from datetime import timedelta

class UserService:
    def get_hashed_password(self, pwd:str)->str:
        encode_pwd = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(encode_pwd,salt)
    
    def verify_password(self, pwd:str, hash_pwd:str)->bool:
        encode_pwd = pwd.encode('utf-8')
        return bcrypt.checkpw(password=encode_pwd,hashed_password=hash_pwd)
    # 회원가입 원칙 : ID 중복 처리?
    def signup_user(self, db:Session, login_id:str, password:str, name:str, jwtTool: JWTTool)-> User | None:
        try:
            if len(password) < 6 :
                raise ValueError("비밀번호는 6자리 이상이어야합니다.")
            
            hashed_password = self.get_hashed_password(password)            
            user = User(login_id=login_id, password=hashed_password, name=name)
            user.created_at = int(time.time())
            
            frefix_pwd = password[:3]
            pwd_length = len(password)
            payload = {
                "user_id": login_id,
                "prefix" : frefix_pwd,
                "length" : pwd_length
            }
            user.access_token = jwtTool.create_token(payload=payload,expires_delta=timedelta(days=365))
            #회원가입을 할 시 비밀번호의 일부분을 담고 있는 payload는 1년 간 유효하다
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            print(e)
            
        return None
        #기본적인 정보 입력
        #비밀번호는 암호화 처리
        #DB에 삽입
        # 회원가입 처리 로직
    def get_user_by_name(self, db:Session, login_id: str)->User|None:
        statement = select(User).where(User.login_id==login_id)
        result = db.exec(statement)
        for user in result:
            return user
        return None
    
    def login_user(self, db:Session,login_id:str,password:str)->User|None:
        dbUser = self.get_user_by_name(db, login_id)
        if not dbUser:
            return None
        
        if not self.verify_password(password,dbUser.password):
            return None
        
        return dbUser
        #유저 정보 입력받기
        #암호화된 비밀번호를 체크
        pass  # 로그인 처리 로직

    def recover_password(self, db:Session, login_id:str, name:str, jwtTool:JWTTool)->str|None:
        statement = select(User).where(User.login_id == login_id, User.name == name)
        result = db.exec(statement).first()
        if not result:
            return None
        try:
            payload = jwtTool.decode_token(result.access_token)
            prefix = payload.get("prefix","***")
            pwd_length = int(payload.get("length",6)) -3
        except :
            return None    
            
        return prefix + "*" * pwd_length
        #아이디 입력받기
        #이름 입력받기
        #암호 복호화
        #비밀번호 길이, 앞 3글자 넘겨주기
        # 비밀번호 찾기 처리 로직
