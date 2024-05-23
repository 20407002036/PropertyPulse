#!/usr/bin/python3

from db_storage import DBStorage
from sqlalchemy import create_engine, MetaData
from db_storage import Base
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User, Base
from property import Property
from reviews import Review

# Create an engine that connects to the MySQL database
engine = create_engine('mysql+mysqldb://root:10229101151@192.168.1.6/flask_property_pulse')

# Create all tables in the database
Base.metadata.create_all(engine)
