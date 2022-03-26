from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from app.database.base import SessionLocal
from app.database.schemas import media
from app.service import media_service

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/media/", response_model=list[media.Media])
def get_media_items(db: Session = Depends(get_db)):
    return media_service.get_all_media(db)


@app.get("/media/{item}", response_model=media.Media)
def get_media_item(item: str, db: Session = Depends(get_db)):
    media_item = media_service.get_media(db, item)
    if media_item is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Media item not found")
    return media_item


@app.post("/media/", response_model=media.Media)
def create_media_item(media_item: media.MediaCreate, db: Session = Depends(get_db)):
    return media_service.create_media(db, media_item)
