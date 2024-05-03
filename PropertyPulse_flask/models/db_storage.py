#!/usr/bin/python3
"""
Database engine
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from .user import User
from .property import Property
# from .base_model import Base
from hashlib import md5


# from .Users import models
# from . import storage


class DBStorage:
    """
        handles long term storage of all class instances
    """
    CNC = {
        # 'Amenity': amenity.Amenity,
        # 'City': city.City,
        # 'Place': place.Place,
        # 'Review': review.Review,
        # 'State': state.State,
        'User': User,
        'Property': Property
    }

    """
        handles storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            creates the engine self.__engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('MYSQL_USER'),
                os.getenv('MYSQL_PWD'),
                os.getenv('MYSQL_HOST'),
                os.getenv('MYSQL_DB')))
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        # if os.environ.get("HBNB_ENV") == 'test':
        #     Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
           returns a dictionary of all objects

           TODO: review this function
        """
        obj_dict = {}
        if cls is not None:
            a_query = self.__session.query(DBStorage.CNC[cls].values())
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in DBStorage.CNC.values():
            a_query = self.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict

    def new(self, obj):
        """
            adds objects to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commits all changes of current database session
        """
        self.__session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self):
        """
           deletes all stored objects, for testing purposes
        """
        for c in DBStorage.CNC.values():
            a_query = self.__session.query(c)
            all_objs = [obj for obj in a_query]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        # Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()

    def get(self, cls, id):
        """
            retrieves one object based on class name and id
        """
        query = self.__session.query(cls).filter_by(id=id)

        obj = query.first()
        return obj

    def count(self, cls=None):
        """
            returns the count of all objects in storage
        """
        obj_dict = models.storage.all(cls)
        return len(obj_dict)
    @staticmethod
    def authenticate_user(self, username, password):
        user = self.__session.query(User).filter(User.username == username, User.password == md5(password.encode()).hexdigest()).first()

        if user:
            return user
        else:
            print("None")
            return None
