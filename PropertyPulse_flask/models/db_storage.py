#!/usr/bin/python3
"""
Database engine
"""

# from .base_model import Base
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
# from .property import Property
from hashlib import md5

Base = declarative_base()


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
        # 'User': User,
        # 'Property': Property
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

        load_dotenv()

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('MYSQL_USER'),
                os.getenv('MYSQL_PWD'),
                os.getenv('MYSQL_HOST'),
                os.getenv('MYSQL_DB')))

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

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
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

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
        pass
        # obj_dict = models.storage.all(cls)
        # return len(obj_dict)
        
    def all_properties(self):
        """
        Retrieve all properties from the Property table.

        Returns:
            A dictionary containing all properties retrieved from the Property table.
         """
        from .property import Property
        from .user import User
         
        obj_dict = {}
        # Query all objects from the Property table
        a_query = self.__session.query(User)
        for prop in a_query:
            obj_ref = f"{type(prop).__name__}.{prop.id}"
            obj_dict[obj_ref] = prop
            return obj_dict

    @staticmethod
    def authenticate_user(self, username, password):
        from .user import User

        authuser = self.__session.query(User).filter(User.username == username,
                                                     User.password == md5(password.encode()).hexdigest()).first()

        if authuser:
            return authuser
        else:
            print("None")
            return None
