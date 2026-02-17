from pydantic import BaseModel, HttpUrl

class URLShortenRequest(BaseModel):
    long_url: HttpUrl