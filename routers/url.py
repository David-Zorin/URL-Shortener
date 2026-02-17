from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
import asyncpg
from database import get_db
from schemas.url import URLShortenRequest
from service.url import encode_short_code, decode_short_code

router = APIRouter()

# Health check endpoint
@router.get("/db_health")
async def health_check(conn: asyncpg.Connection = Depends(get_db)):
    try:
        await conn.fetchval("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")
    
#show all database
@router.get("/show_db")
async def show_database(conn: asyncpg.Connection = Depends(get_db)):
    try:
        query= "select * from urls"
        data = await conn.fetch(query)
        return [dict(row) for row in data]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


  
#create and save new short url, if exist return it instantly
@router.post("/shorten")
async def shorten_url(
    payload: URLShortenRequest, 
    conn: asyncpg.Connection = Depends(get_db)
):
    try:
        #check if url alredy saved in db
        long_url_str = str(payload.long_url)
        check_existing_query = "select id, short_code from urls where original_url = $1"
        url_id = await conn.fetchrow(check_existing_query, long_url_str)
        if url_id:
            return {
                "short_code": url_id["short_code"],
                "original_url": payload.long_url
            }

        insert_query = "INSERT INTO urls (original_url) VALUES ($1) RETURNING id"
        url_id = await conn.fetchval(insert_query, long_url_str)

        #short code to return
        short_code = encode_short_code(url_id)

        #update the short_code
        update_query = "UPDATE urls SET short_code = $1 WHERE id = $2"
        await conn.execute(update_query, short_code, url_id)

        return {
            "short_code": short_code,
            "original_url": payload.long_url
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#redirect to the relevant url
@router.get("/{short_code}")
async def redirect_to_url(
    short_code: str, 
    conn: asyncpg.Connection = Depends(get_db)
):
    # extra safe guards if it suddenly try to call get with /shorten
    if short_code == "shorten":
        raise HTTPException(
            status_code=405, 
            detail="To shorten a URL, use a POST request via Postman or /docs."
        )
    
    try:
        url_id = decode_short_code(short_code)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid short code format")

    query = """
        UPDATE urls 
        SET times_used = times_used + 1 
        WHERE id = $1 
        RETURNING original_url
    """
    long_url = await conn.fetchval(query, url_id)

    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=long_url)


#see the stats (amount of redirects)
@router.get("/stats/{short_code}")
async def get_stats(short_code: str, conn = Depends(get_db)):
    query = "SELECT original_url, times_used, created_at FROM urls WHERE short_code = $1"
    row = await conn.fetchrow(query, short_code)
    if not row:
        raise HTTPException(status_code=404, detail="Link not found")
        
    return {
        "short_code": short_code,
        "original_url": row["original_url"],
        "clicks": row["times_used"],
        "created_at": row["created_at"]
    }