#!/usr/bin/python3

# from .models import DBStorage
from sqlalchemy import create_engine, MetaData
from models.db_storage import Base
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.property import Property
from models.reviews import Review

# Create an engine that connects to the MySQL database
engine = create_engine('mysql+mysqldb://mitsudata:10229101151@localhost/flask_property_pulse')

# Create all tables in the database
Base.metadata.create_all(engine)
