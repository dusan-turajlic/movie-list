from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.engine import Connectable
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED

from app.database.base import engine
from app.database.schemas import media
from app.database.schemas import actor
from app.service import media_service
from app.service import actor_service

app = FastAPI()


# Dependency
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()


@app.get("/media", response_model=list[media.Media])
def get_media_items(db: Connectable = Depends(get_db)):
    return media_service.get_all_media(db)


@app.get("/media/{item}", response_model=media.Media)
def get_media_item(item: str, db: Connectable = Depends(get_db)):
    media_item = media_service.get_media(db, item)
    if media_item is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Media item not found")
    return media_item


@app.post("/media", response_model=media.Media, status_code=HTTP_201_CREATED)
def create_media_item(media_item: media.MediaCreate, db: Connectable = Depends(get_db)):
    return media_service.create_media(db, media_item)


@app.get("/actors", response_model=list[actor.Actor])
def get_actors(db: Connectable = Depends(get_db)):
    return actor_service.get_all_actors(db)


@app.get("/actors/{actor}", response_model=actor.Actor)
def get_actor(actor: str, db: Connectable = Depends(get_db)):
    media_item = actor_service.get_actor(db, actor)
    if media_item is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Media item not found")
    return media_item


@app.post("/actors", response_model=actor.Actor, status_code=HTTP_201_CREATED)
def create_actor(media_item: actor.ActorCreate, db: Connectable = Depends(get_db)):
    return actor_service.create_actor(db, media_item)
