from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQLコンテナへの接続URLを設定
DATABASE_URL = "mysql+pymysql://root:@db/demo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()