from fastapi.testclient import TestClient
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.database.schemas.actor import ActorCreate
from app.database.tables import actor
from app.main import app
from app.service import actor_service
from test.utils.db_utils import check_exists_in_database, clean_up

client = TestClient(app)


def test_create_actor(database):
    firstname = "John"
    lastname = "Doe"
    response = client.post("/actors/", json={"firstname": firstname, "lastname": lastname})
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
    response = client.get("/actors/")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 4

    for item in actor_items:
        clean_up(database, actor, item['slug'])
