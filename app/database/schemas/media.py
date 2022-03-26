from pydantic import BaseModel


class MediaBase(BaseModel):
    type: int
    rating: int


class MediaCreate(MediaBase):
    pass


class Media(MediaBase):
    slug: str

    class Config:
        orm_mode = True
