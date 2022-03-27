import uuid

from sqlalchemy import select
from sqlalchemy.engine import Connectable

from app.database.schemas.actor import ActorCreate
from app.database.tables import actor


def get_actor(db: Connectable, actor_slug: str):
    query = select(actor).where(actor.c.slug == actor_slug)
    return db.execute(query).mappings().first()


def get_all_actors(db: Connectable):
    return db.execute(select(actor)).mappings().all()


def create_actor(db: Connectable, actor_data: ActorCreate):
    actor_data = {"slug": str(uuid.uuid4()), **actor_data.dict()}
    insert = actor.insert().values(**actor_data)
    db.execute(insert)
    return actor_data
