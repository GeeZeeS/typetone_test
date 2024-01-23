from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class UrlShortenCreate(BaseModel):
    url: HttpUrl
    shortcode: Optional[str] = ""


class UrlShortenResponse(BaseModel):
    shortcode: str


class UrlStatsResponse(CamelModel):
    created: datetime
    last_redirect: Optional[datetime]
    redirect_count: int
