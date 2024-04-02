"""This is the User module that inherits from the Base"""
from models.base_model import BaseModel


class User(BaseModel):
    """Handles the User class"""
    # Public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""