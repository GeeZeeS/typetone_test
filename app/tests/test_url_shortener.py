import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from core.database import get_db, Base
from core.pytest_config import override_get_db, engine
from apps.url_shortener.routers import shorten_url_router

Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(shorten_url_router)
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client


def test_create_shorten_url(client):
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/", "shortcode": "abc123"},
    )
    assert response.status_code == 201
    assert response.json() == {"shortcode": "abc123"}


def test_create_shorten_url_random_shortcode(client):
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/"},
    )
    assert response.status_code == 201
    assert "shortcode" in response.json()


def test_create_shorten_url_conflict(client):
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/", "shortcode": "abc123"},
    )
    assert response.status_code == 409


def test_create_shorten_url_invalid_shortcode(client):
    response = client.post(
        "/shorten",
        json={"url": "https://www.google.com/", "shortcode": "invalid_shortcode"},
    )
    assert response.status_code == 412


def test_redirect_to_url(client):
    response = client.get("/abc123", follow_redirects=False)
    assert response.headers["Location"] == "https://www.google.com/"
    assert response.status_code == 302


def test_url_stats(client):
    response = client.get("/abc123/stats")
    assert response.status_code == 200
    assert "created" in response.json()
    assert "lastRedirect" in response.json()
    assert "redirectCount" in response.json()
