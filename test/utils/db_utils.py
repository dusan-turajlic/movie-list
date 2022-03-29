from sqlalchemy import Table, select, delete
from sqlalchemy.engine import Connectable


def check_exists_in_database(db: Connectable, table: Table, slug: str):
    result = db.execute(
        select(table).where(table.c.slug == slug)
    ).mappings().first()

    assert result is not None


def clean_up(db: Connectable, table: Table, slug: str):
    db.execute(
        delete(table).where(table.c.slug == slug)
    )
