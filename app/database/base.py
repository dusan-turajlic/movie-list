from os import getenv

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
    user=getenv('DB_USERNAME', 'movielist'),
    password=getenv('DB_PASSWORD', 'movielist'),
    host=getenv('DB_HOST', 'postgres'),
    port=getenv('DB_PORT', '5432'),
    database=getenv('DB_DATABASE', 'movielist')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
