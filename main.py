from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import init_db_pool, close_db_pool, db_pool

app = FastAPI()

# Initialize and close database pool on startup/shutdown
#Run when the app starts
@app.on_event("startup")
async def startup_event():
    await init_db_pool()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_pool()

@app.get("/")
async def read_root():
    return {"message": "URL Shortener API is running!"}

# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        async with db_pool.acquire() as conn:
            #Query here
            await conn.fetchval("SELECT 1")
        return JSONResponse({"status": "healthy", "database": "connected"})
    except Exception as e:
        return JSONResponse(
            {"status": "unhealthy", "database": "disconnected", "error": str(e)},
            status_code=500
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)