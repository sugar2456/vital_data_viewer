# プロジェクト構成

```
├── app/ ... アプリケーション（API）のコード群
├── db/  ... マイグレーション・シード用のファイル群
└── log/ ... DBコンテナのログ出力用
```

## APP配下のフォルダ

```
└── app
    ├── __init__.py
    ├── cruds ... DBにクエリを投げる処理。routers/内から呼び出される
    ├── database.py ... DBセッションの実装
    ├── models ... sqlalchemy を用いたモデル定義
    ├── routers ... @app.get や @router.get などの実装
    ├── schemas ... pydantic を用いたモデルスキーマ定義
    └── utils ... 汎用的なスクリプトなど
```

## 起動コマンド

```
uvicorn main:app --reload
```

## マイグレーションファイル最新ファイルまで実行

```
alembic upgrade head
```

## テストコードの実行

```
cd /app
pytest
```

参考  
https://qiita.com/woods0918/items/2d7b2421d8a8f1b6d724
https://note.com/yusugomori/n/n9f2c0422dfcd