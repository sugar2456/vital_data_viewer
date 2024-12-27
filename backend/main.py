from fastapi import FastAPI, Request, Depends
from strawberry.fastapi import GraphQLRouter
from app.api.graphql.schema import schema
from fastapi.responses import JSONResponse
from app.config import settings
from starlette.middleware.sessions import SessionMiddleware
import requests
import base64

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(f"secret : {settings.fitbit_client_secret}")
app.add_middleware(SessionMiddleware, secret_key=settings.fitbit_client_secret)

@app.get("/auth/confirm")
async def auth_confirm(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    print(f"code: {code}")
    print(f"state: {state}")
    
    if code:
        # 認証コードを使用してトークンを取得する
        client_id = settings.fitbit_client_id
        client_secret = settings.fitbit_client_secret
        redirect_uri = settings.fitbit_redirect_uri
        authorization = f"{client_id}:{client_secret}"
        base64encoded = base64.b64encode(authorization.encode()).decode()
        authorization_header = f"Basic {base64encoded}"
        
        headers = {
            'Authorization': authorization_header,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'client_id': client_id,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code,
            'code_verifier': 'your_code_verifier'  # ここに実際のcode_verifierを設定してください
        }
        
        response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)
        
        if response.status_code == 200:
            return JSONResponse(content=response.json())
        else:
            return JSONResponse(content={"error": "トークン取得に失敗しました", "details": response.json()}, status_code=response.status_code)
    else:
        return JSONResponse(content={"error": "認証コードが見つかりませんでした"}, status_code=400)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)