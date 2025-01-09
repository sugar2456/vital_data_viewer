from fastapi import FastAPI, Depends
from src.api.endpoints import fitbit_auth
from src.api.endpoints import fitbit_activity

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])
app.include_router(fitbit_activity.router, prefix="/api", tags=["fitbit_activity"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)