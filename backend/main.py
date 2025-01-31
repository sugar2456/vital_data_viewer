from fastapi import FastAPI
from src.api.endpoints import fitbit_activity, fitbit_auth, fitbit_heart_rate, fitbit_calories, fitbit_food, fitbit_sleep, fitbit_weight, fitbit_devices, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(fitbit_auth.router, prefix="/api", tags=["fitbit_auth"])
app.include_router(fitbit_activity.router, prefix="/api", tags=["fitbit_activity"])
app.include_router(fitbit_heart_rate.router, prefix="/api", tags=["fitbit_activity"])
app.include_router(fitbit_calories.router, prefix="/api", tags=["fitbit_calories"])
app.include_router(fitbit_food.router, prefix="/api", tags=["fitbit_food"])
app.include_router(fitbit_sleep.router, prefix="/api", tags=["fitbit_sleep"])
app.include_router(fitbit_weight.router, prefix="/api", tags=["fitbit_weight"])
app.include_router(fitbit_devices.router, prefix="/api", tags=["fitbit_devices"])
app.include_router(users.router, prefix="/api", tags=["users"])

origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド
    allow_headers=["*"],  # 許可するHTTPヘッダー
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)