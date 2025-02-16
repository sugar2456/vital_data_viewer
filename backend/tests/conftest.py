import pytest
import sys
import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
from src.db.session import Base


# conftest.pyのあるディレクトリパス
conftest_dir = os.path.dirname(__file__)
# プロジェクトのルートディレクトリパス（絶対パス）
project_root = os.path.abspath(os.path.join(conftest_dir, '..'))
# プロジェクトのルートディレクトリパスをパスに追加
sys.path.insert(0,project_root)
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

test_database_user = os.getenv("TEST_DB_USERNAME", "root")
test_database_host = os.getenv("TEST_DB_HOSTNAME", "test_db")
test_database_db_name = os.getenv("TEST_DB_NAME", "test_demo")
SQLALCHEMY_TEST_DATABASE_URL = f"mysql+pymysql://{test_database_user}:@{test_database_host}/{test_database_db_name}"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

@pytest.fixture(scope="module")
def db_session():
    print("セッション作成")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    print("テーブルリセット", inspector.get_table_names())
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
