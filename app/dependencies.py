from sqlalchemy.engine import Connectable

from app.database.base import engine


# Dependency
def get_db() -> Connectable:
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()
