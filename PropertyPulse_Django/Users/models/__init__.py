#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
# from . import models # type: ignore


# storage_t = getenv("HBNB_TYPE_STORAGE")


from .db_storage import DBStorage

storage = DBStorage()

# storage.reload()


def CNC():
    return None
