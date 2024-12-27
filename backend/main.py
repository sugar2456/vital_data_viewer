from fastapi import FastAPI, Request, Depends
from strawberry.fastapi import GraphQLRouter
from app.api.graphql.schema import schema
from fastapi.responses import JSONResponse
from app.config import settings
from starlette.middleware.sessions import SessionMiddleware
import requests
import base64
from app.api.endpoints import fitbit_auth

graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)