from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.database import SQLALCHEMY_URL

Base = declarative_base()
engine = create_engine(SQLALCHEMY_URL)
DBSession = sessionmaker(bind=engine)
