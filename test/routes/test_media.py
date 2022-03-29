from fastapi.testclient import TestClient
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.database.schemas.media import MediaCreate
from app.database.tables import media
from app.main import app
from app.resources.enum import MediaType
from app.service import media_service
from test.utils.db_utils import check_exists_in_database, clean_up

client = TestClient(app)


def test_create_media_item(database):
    response = client.post("/media/", json={"type": int(MediaType.MOVIE), "rating": 3})
    assert response.status_code == HTTP_201_CREATED
    json = response.json()

    assert json["type"] == int(MediaType.MOVIE)
    assert json["rating"] == 3
    assert json["slug"] is not None

    check_exists_in_database(database, media, json["slug"])
    clean_up(database, media, json["slug"])


def test_get_a_media_item(database):
    media_item = media_service.create_media(database, MediaCreate(type=int(MediaType.TV_SERIES), rating=4))
    assert media_item is not None
    response = client.get("/media/" + media_item["slug"])

    assert response.status_code == HTTP_200_OK

    clean_up(database, media, media_item["slug"])


def test_get_all_media_items(database):
    media_items = [
        media_service.create_media(database, MediaCreate(type=int(MediaType.TV_SERIES), rating=4)),
        media_service.create_media(database, MediaCreate(type=int(MediaType.TV_SERIES), rating=4)),
        media_service.create_media(database, MediaCreate(type=int(MediaType.TV_SERIES), rating=4)),
        media_service.create_media(database, MediaCreate(type=int(MediaType.TV_SERIES), rating=4)),
    ]
    response = client.get("/media/")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 4

    for item in media_items:
        clean_up(database, media, item['slug'])
