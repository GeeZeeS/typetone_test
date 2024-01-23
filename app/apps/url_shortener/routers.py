from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse

from core.database import get_db
from .queries import filter_shorten_url, create_shorten_url, update_shorten_url
from .schemas import UrlShortenResponse, UrlShortenCreate, UrlStatsResponse
from .scripts import validate_shortcode, generate_shortcode

shorten_url_router = APIRouter(
    prefix="",
    tags=["shorten_url"],
    responses={404: {"description": "Not found"}},
)


@shorten_url_router.post("/shorten", response_model=UrlShortenResponse, status_code=status.HTTP_201_CREATED)
def shorten_url(url_shorten: UrlShortenCreate, db: Session = Depends(get_db)):
    if url_shorten.shortcode:
        if filter_shorten_url(db, url_shorten.shortcode):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Shortcode already in use"
            )
        if not validate_shortcode(url_shorten.shortcode):
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED, detail="The provided shortcode is invalid"
            )
    else:
        url_shorten.shortcode = generate_shortcode()
    db_url_shorten = create_shorten_url(db, url_shorten)
    return db_url_shorten


@shorten_url_router.get("/{shortcode}")
def redirect_to_url(shortcode: str, db: Session = Depends(get_db)):
    db_url_shorten = filter_shorten_url(db, shortcode)
    if not db_url_shorten:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Shortcode not found"
        )

    url_record = update_shorten_url(db, db_url_shorten)
    return RedirectResponse(url=url_record.url, status_code=302)


@shorten_url_router.get("/{shortcode}/stats", response_model=UrlStatsResponse, status_code=status.HTTP_200_OK)
def url_stats(shortcode: str, db: Session = Depends(get_db)):
    db_url_shorten = filter_shorten_url(db, shortcode)
    if not db_url_shorten:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Shortcode not found"
        )
    return db_url_shorten
