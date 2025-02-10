from sqlmodel import (SQLModel,Session, create_engine)

db_url = 'sqlite:///./app/db/test.db'
db_engine = create_engine(db_url, connect_args={"check_same_thread": False})

def get_db():
  with Session(db_engine) as session:
    yield session
  
def create_db():
  SQLModel.metadata.create_all(db_engine)