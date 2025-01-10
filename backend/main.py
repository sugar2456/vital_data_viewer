from fastapi import FastAPI
from src.api.endpoints import fitbit_auth, fitbit_steps, fitbit_heart_rate

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])
app.include_router(fitbit_steps.router, prefix="/api", tags=["fitbit_activity"])
app.include_router(fitbit_heart_rate.router, prefix="/api", tags=["fitbit_activity"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)