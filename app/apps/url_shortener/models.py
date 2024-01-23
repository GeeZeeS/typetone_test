from sqlalchemy import (
    Column, Integer, String,
    DateTime, func
)

from core.database import Base


class UrlShorten(Base):
    __tablename__ = 'url_shorten'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    shortcode = Column(String, unique=True, index=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    last_redirect = Column(DateTime(timezone=True), nullable=True)
    redirect_count = Column(Integer, default=0)
