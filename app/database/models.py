from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    type = Column(Integer, index=True)
    rating = Column(Integer)


class Actor(Base):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
