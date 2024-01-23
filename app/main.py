from fastapi import FastAPI

from apps.url_shortener.routers import shorten_url_router

app = FastAPI(title="TypeTone")

app.include_router(shorten_url_router)
