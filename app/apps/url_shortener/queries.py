from datetime import datetime

from sqlalchemy.orm import Session

from apps.url_shortener.models import UrlShorten
from apps.url_shortener.schemas import UrlShortenCreate


def create_shorten_url(db: Session, url_shorten: UrlShortenCreate) -> UrlShorten:
    db_url_shorten = UrlShorten(url=str(url_shorten.url), shortcode=url_shorten.shortcode)
    db.add(db_url_shorten)
    db.commit()
    db.refresh(db_url_shorten)
    return db_url_shorten


def filter_shorten_url(db: Session, shortcode: str) -> UrlShorten:
    return db.query(UrlShorten).filter(UrlShorten.shortcode == shortcode).first() # noqa


def update_shorten_url(db: Session, db_url_shorten: UrlShorten) -> UrlShorten:
    db_url_shorten.last_redirect = datetime.utcnow()
    db_url_shorten.redirect_count = db_url_shorten.redirect_count + 1
    db.commit()
    db.refresh(db_url_shorten)
    return db_url_shorten
