#!/usr/bin/python3
""" holds class User"""

# import models
from .base_model import BaseModel
from .storage import Base
# from os import getenv
# import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin


# removed Base from the inherit bracket
class User(BaseModel, Base, UserMixin):
    """Representation of a user """

    __tablename__ = 'users'

    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    properties = relationship('Property', back_populates='user')
    reviews = relationship('Review', back_populates='user')

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def get_id(self):
        return self.id
    
    
    @staticmethod
    def authenticate_user(self, username, password):
        user = self.__session.query(User).filter(User.username == username, User.password == md5(password.encode()).hexdigest()).first()

        if user:
            return user
        else:
            print("None")
            return None
