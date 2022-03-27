import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select, delete, Table
from sqlalchemy.engine import Connectable
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.database.base import engine
from app.database.schemas.actor import ActorCreate
from app.database.schemas.media import MediaCreate
from app.database.tables import actor
from app.database.tables import media
from app.main import app
from app.resources.enum import MediaType
from app.service import media_service, actor_service

client = TestClient(app)


@pytest.fixture
def database():
    db = engine.connect()
    yield db
    db.close()


def check_exists_in_database(db: Connectable, table: Table, slug: str):
    result = db.execute(
        select(table).where(table.c.slug == slug)
    ).mappings().first()

    assert result is not None


def clean_up(db: Connectable, table: Table, slug: str):
    db.execute(
        delete(table).where(table.c.slug == slug)
    )


def test_create_media_item(database):
    response = client.post("/media", json={"type": int(MediaType.MOVIE), "rating": 3})
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
    response = client.get("/media")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 4

    for item in media_items:
        clean_up(database, media, item['slug'])


def test_create_actor(database):
    firstname = "John"
    lastname = "Doe"
    response = client.post("/actors", json={"firstname": firstname, "lastname": lastname})
    assert response.status_code == HTTP_201_CREATED
    json = response.json()

    assert json["firstname"] == "John"
    assert json["lastname"] == "Doe"
    assert json["slug"] is not None

    check_exists_in_database(database, actor, json["slug"])
    clean_up(database, actor, json["slug"])


def test_get_a_actor(database):
    actor_item = actor_service.create_actor(database, ActorCreate(firstname="Tony", lastname="Stark"))
    assert actor_item is not None
    response = client.get("/actors/" + actor_item["slug"])

    assert response.status_code == HTTP_200_OK

    clean_up(database, actor, actor_item["slug"])


def test_get_all_actors(database):
    actor_items = [
        actor_service.create_actor(database, ActorCreate(firstname="Tony", lastname="Stark")),
        actor_service.create_actor(database, ActorCreate(firstname="Tony", lastname="Stark")),
        actor_service.create_actor(database, ActorCreate(firstname="Tony", lastname="Stark")),
        actor_service.create_actor(database, ActorCreate(firstname="Tony", lastname="Stark")),
    ]
    response = client.get("/actors")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 4

    for item in actor_items:
        clean_up(database, actor, item['slug'])
