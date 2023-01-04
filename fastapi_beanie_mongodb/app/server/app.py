from fastapi import FastAPI

from .database import init_db
from .routes import router

app = FastAPI()
app.include_router(router, tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
