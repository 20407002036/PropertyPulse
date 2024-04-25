#!/usr/bin/python3
"""
This method creates an instance of the FileStorage class for managing data.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
