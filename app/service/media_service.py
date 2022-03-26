import uuid

from sqlalchemy.orm import Session

from app.database.models import Media
from app.database.schemas.media import MediaCreate


def get_media(db: Session, media_id: str):
    return db.query(Media).filter(Media.uuid == media_id).first()


def get_all_media(db: Session):
    return db.query(Media).all()


def create_media(db: Session, media_item: MediaCreate):
    db_media_item = Media(slug=uuid.uuid4(), type=media_item.type, rating=media_item.rating)
    db.add(db_media_item)
    db.commit()
    db.refresh(db_media_item)

    return db_media_item


