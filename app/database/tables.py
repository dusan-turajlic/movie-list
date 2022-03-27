from sqlalchemy import Table, Column, ForeignKey, Integer, String, MetaData

metadata_obj = MetaData()

actor = Table(
    "actor",
    metadata_obj,
    Column("id", Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
    Column("slug", String(36), nullable=False, unique=True, index=False),
    Column("firstname", String(35), nullable=False, index=False),
    Column("lastname", String(35), nullable=False, index=False)
)

media = Table(
    "media",
    metadata_obj,
    Column("id", Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
    Column("slug", String(36), nullable=False, unique=True, index=False),
    Column("type", Integer, nullable=False, index=True),
    Column("rating", Integer, nullable=True, index=False)
)

actor_media = Table(
    "actor_media",
    metadata_obj,
    Column("actor_id", Integer, ForeignKey("actor.id"), nullable=False, index=True),
    Column("media_id", Integer, ForeignKey("media.id"), nullable=False, index=True)
)

media_translations = Table(
    "media_translation",
    metadata_obj,
    Column("id", Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
    Column("language", Integer, nullable=False, index=True),
    Column("name", Integer, nullable=False, index=True),
    Column("value", String(500), nullable=False, index=False),
    Column("media_id", Integer, ForeignKey("media.id"), nullable=False, index=True)
)
