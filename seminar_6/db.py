import databases
import sqlalchemy as sa
from fastapi import FastAPI
from settings import settings

DATABASE_URL = "sqlite:///mydatabase.db"
DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()




users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer,
    primary_key=True),
    sa.Column("username", sa.String(32)),
    sa.Column("email", sa.String(128)),
    sa.Column("password", sa.String(128)),
)
engine = sa.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
