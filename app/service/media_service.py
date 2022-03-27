import uuid

from sqlalchemy import select
from sqlalchemy.engine import Connectable

from app.database.schemas.media import MediaCreate
from app.database.tables import media


def get_media(db: Connectable, media_slug: str):
    query = select(media).where(media.c.slug == media_slug)
    return db.execute(query).mappings().first()


def get_all_media(db: Connectable):
    result = db.execute(select(media))
    return result.mappings().all()


def create_media(db: Connectable, media_item: MediaCreate):
    media_item = {"slug": str(uuid.uuid4()), **media_item.dict()}
    insert = media.insert().values(**media_item)
    db.execute(insert)
    return media_item

