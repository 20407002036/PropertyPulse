#!/usr/bin/python3
""" holds class User"""

# import models
from .base_model import BaseModel
from .storage import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin



class User(BaseModel, Base, UserMixin):
    """Representation of a user """

    __tablename__ = 'users'

    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationshot btwn properties and users table
    properties = relationship('Property', backref='user')

    # One to many relationship with reviews
    reviews = relationship('Review', backref='user')
    

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
    
    
