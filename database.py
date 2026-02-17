import asyncpg
import os
from fastapi import HTTPException

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://MyName:MyPass@localhost:5432/shortener')
db_pool = None
MIN_SIZE = 1
MAX_SIZE = 10

#Initialize the connection pool when the app starts
async def init_db_pool():
    global db_pool
    try:
        db_pool = await asyncpg.create_pool(
            DATABASE_URL,
            min_size = MIN_SIZE,
            max_size = MAX_SIZE
        )
        print("Database pool initialized successfully")
    except Exception as e:
        print(f"Warning: Failed to initialize database pool: {e}")
        print("App will run but database routes will fail")

#Close the connection pool when the app stop
async def close_db_pool():
    global db_pool
    if db_pool:
        await db_pool.close()
        print("Database pool closed")

async def get_db():
    """
    Dependency that provides a database connection from the pool.
    It automatically handles error checking and connection release.
    """
    if db_pool is None:
        raise HTTPException(
            status_code=500, 
            detail="Database pool not initialized"
        )
    # Acquire a connection from the pool
    async with db_pool.acquire() as connection:
        yield connection