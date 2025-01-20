from fastapi import FastAPI
from src.api.endpoints import fitbit_activity, fitbit_auth, fitbit_heart_rate, fitbit_sleep, fitbit_weight, fitbit_devices

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])
app.include_router(fitbit_activity.router, prefix="/api", tags=["fitbit_activity"])
app.include_router(fitbit_heart_rate.router, prefix="/api", tags=["fitbit_activity"])
app.include_router(fitbit_sleep.router, prefix="/api", tags=["fitbit_sleep"])
app.include_router(fitbit_weight.router, prefix="/api", tags=["fitbit_weight"])
app.include_router(fitbit_devices.router, prefix="/api", tags=["fitbit_devices"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)