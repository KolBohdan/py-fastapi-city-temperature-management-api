from fastapi import FastAPI

from src.city.router import router as city_router

app = FastAPI()

app.include_router(city_router)


@app.get("/")
def read_root():
    return {
        "message": "It isFastAPI application "
                   "that manages city data and "
                   "their corresponding temperature data",
    }

