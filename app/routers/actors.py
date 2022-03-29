from fastapi import APIRouter, Depends
from sqlalchemy.engine import Connectable
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED

from app.database.schemas.actor import Actor, ActorCreate
from app.dependencies import get_db
from app.service.actor_service import get_all_actors, create_actor, get_actor

router = APIRouter(
    prefix="/actors",
    tags=["actors"],
    responses={HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/", response_model=list[Actor])
async def index(db: Connectable = Depends(get_db)):
    return get_all_actors(db)


@router.get("/{uuid}", response_model=Actor)
async def show(uuid: str, db: Connectable = Depends(get_db)):
    return get_actor(db, uuid)


@router.post("/", response_model=Actor, status_code=HTTP_201_CREATED)
async def store(media_item: ActorCreate, db: Connectable = Depends(get_db)):
    return create_actor(db, media_item)
