from os import getenv

from peewee import PostgresqlDatabase, Model

DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')

DB_DATABASE = getenv('DB_DATABASE')
DB_USERNAME = getenv('DB_USERNAME')
DB_PASSWORD = getenv('DB_PASSWORD')

psql_db = PostgresqlDatabase(DB_DATABASE, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = psql_db
