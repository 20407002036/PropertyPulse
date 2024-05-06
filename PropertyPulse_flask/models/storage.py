#!/usr/bin/python3
"""
This method creates an instance of the FileStorage class for managing data.
"""
from .db_storage import DBStorage

storage = DBStorage()
storage.reload()
