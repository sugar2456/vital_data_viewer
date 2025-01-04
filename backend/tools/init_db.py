from src.db.session import engine, Base
from src.models.user import User

Base.metadata.create_all(bind=engine)

print("テーブルを作成しました")