from fastapi import APIRouter, Depends
from sqlalchemy.engine import Connectable
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED

from app.database.schemas.media import Media, MediaCreate
from app.dependencies import get_db
from app.service.media_service import get_all_media, get_media, create_media

router = APIRouter(
    prefix="/media",
    tags=["media"],
    responses={HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/", response_model=list[Media])
async def index(db: Connectable = Depends(get_db)):
    return get_all_media(db)


@router.get("/{uuid}", response_model=Media)
async def show(uuid: str, db: Connectable = Depends(get_db)):
    return get_media(db, uuid)


@router.post("/", response_model=Media, status_code=HTTP_201_CREATED)
async def store(media_item: MediaCreate, db: Connectable = Depends(get_db)):
    return create_media(db, media_item)
