from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from config import DB_HOST, DB_USER, DB_PWD

engine = create_engine(f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:5432/episodedb")

if not database_exists(engine.url):
    create_database(engine.url)
