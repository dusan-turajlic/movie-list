from os import getenv

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
    user=getenv('DB_USERNAME', 'postgres'),
    password=getenv('DB_PASSWORD', 'postgres'),
    host=getenv('DB_HOST', 'postgres'),
    port=getenv('DB_PORT', '5432'),
    database=getenv('DB_DATABASE', 'postgres-db')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
