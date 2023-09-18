import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///my_database.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

databases = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI

@app.on_event('startup')
async def startup():
    await databases.connect()

@app.on_event('shutdown')
async def shutdown():
    await databases.disconnect()