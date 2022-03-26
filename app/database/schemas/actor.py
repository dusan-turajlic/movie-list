from pydantic import BaseModel


class ActorBase(BaseModel):
    firstname: str
    lastname: str


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    slug: str

    class Config:
        orm_mode = True
