import uuid

from sqlalchemy.orm import Session

from app.database.models import Actor
from app.database.schemas.actor import ActorCreate


def get_actor(db: Session, actor_id: str):
    return db.query(Actor).filter(Actor.uuid == actor_id).first()


def get_all_actors(db: Session):
    return db.query(Actor).all()


def create_actor(db: Session, actor: ActorCreate):
    db_media_item = Actor(slug=uuid.uuid4(), firstname=actor.firstname, lastname=actor.lastname)
    db.add(db_media_item)
    db.commit()
    db.refresh(db_media_item)

    return db_media_item
