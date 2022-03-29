from fastapi import FastAPI

from app.routers import actors, media

app = FastAPI()

app.include_router(actors.router)
app.include_router(media.router)
