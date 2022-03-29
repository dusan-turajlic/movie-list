import pytest

from app.database.base import engine


@pytest.fixture(scope="session")
def database():
    db = engine.connect()
    yield db
    db.close()
