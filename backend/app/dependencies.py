from sqlmodel import (SQLModel,Session, create_engine)
from datetime import datetime, timedelta, timezone
from jose import jwt
import time 
SECRET_KEY = "MY_SECRET_123456789" #이렇게 설정하는 것은 보안에 취약함(향후 발전 필요)
ALGORITHM = "HS256"
db_url = 'sqlite:///./backend/app/db/banking.db'
db_engine = create_engine(db_url, connect_args={"check_same_thread": False})

def get_db():
  with Session(db_engine) as session:
    yield session
  
def create_db():
  SQLModel.metadata.create_all(db_engine)
  
class JWTTool:
  def create_token(self, payload: dict, expires_delta: timedelta | None = timedelta(minutes=30)):
    payload_to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    payload_to_encode.update({
      'exp' : expire
    })
    return jwt.encode(payload_to_encode,SECRET_KEY,algorithm=ALGORITHM)
  
  def decode_token(self, token:str)-> dict | None :
    try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
      if payload is not None :
        Now = int(time.time())
        ExpireAt = payload.get('exp',0)
        if ExpireAt < Now :
          return None
        return payload
    except:
      pass
    return None


  
