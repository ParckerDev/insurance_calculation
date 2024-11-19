from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database


DATABASE_URL = 'postgresql+asyncpg:///username:password@localhost/dbname'

database = Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()
