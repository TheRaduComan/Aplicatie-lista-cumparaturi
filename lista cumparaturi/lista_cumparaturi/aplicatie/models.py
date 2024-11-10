from django.db import models

# Create your models here.
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

hostname = "127.0.0.1"
username = "root"
password = ""
port = 3306
database = "lista cumparaturi"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Raft(Base):
    __tablename__ = "rafturi"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(200),nullable=False)
    bought = Column(Boolean,default=False,nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Produs:
    pass