from src.db.session import engine, Base
from src.models.user import User
from src.models.pkce_cache import PkceCache

Base.metadata.create_all(bind=engine)

print("テーブルを作成しました")