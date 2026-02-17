import asyncpg
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://MyName:MyPass@localhost:5432/shortener')

# Global connection pool (created at startup, closed at shutdown)
db_pool = None

#Initialize the connection pool when the app starts
async def init_db_pool():
    global db_pool
    try:
        db_pool = await asyncpg.create_pool(
            DATABASE_URL,
            min_size=1, # Minimum 10 connections
            max_size=10 # Maximum 20 connections
        )
        print("Database pool initialized successfully")
    except Exception as e:
        print(f"Failed to initialize database pool: {e}")
        raise

#Close the connection pool when the app stop
async def close_db_pool():
    global db_pool
    if db_pool:
        await db_pool.close()
        print("Database pool closed")