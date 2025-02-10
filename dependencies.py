# 공통 의존성 (DB 연결)
from fastapi import Depends
from sqlmodel import Session, create_engine, select, SQLModel

# 계좌 DB
account_db_file_name = "account.db"
account_db_url = f"sqlite:///{account_db_file_name}"
account_db_conn_args = {"check_same_thread": False}
account_db_engine = create_engine(account_db_url, connect_args=account_db_conn_args)


# 사용자 DB
user_db_file_name = "user.db"
user_db_url = f"sqlite:///{user_db_file_name}"
user_db_conn_args = {"check_same_thread": False}
user_db_engine = create_engine(user_db_url, connect_args=user_db_conn_args)

def get_account_db_session():
    with Session(account_db_engine) as session:
        yield session

def get_user_db_session():
    with Session(user_db_engine) as session:
        yield session

def create_user_db_and_tables():
    SQLModel.metadata.create_all(user_db_engine)

def create_account_db_and_tables():
    SQLModel.metadata.create_all(account_db_engine)