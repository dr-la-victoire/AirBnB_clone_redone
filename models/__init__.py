"""This module is the initialization module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()