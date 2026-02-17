from fastapi import FastAPI
from contextlib import asynccontextmanager
import database
from routers.url import router as url_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    #ON STARTUP
    await database.init_db_pool()
    yield
    #ON SHUTDOWN
    await database.close_db_pool()

app = FastAPI(lifespan=lifespan)

app.include_router(url_router)

@app.get("/")
async def read_root():
    return {"message": "URL Shortener API is running!"}
