from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import get_db_connection, close_db_connection

app = FastAPI()

#root to check if server working
@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running!"}

#check if database is connected
@app.get("/health")
def health_check():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        close_db_connection(conn)
        return JSONResponse({"status": "healthy", "database": "connected"})
    except Exception as e:
        return JSONResponse({"status": "unhealthy", "database": "disconnected", "error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)