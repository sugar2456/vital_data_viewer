from fastapi import FastAPI, Depends
from src.api.endpoints import fitbit_auth

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)