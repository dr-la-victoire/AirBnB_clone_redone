"""This is the City module that inherits from the Base"""
from models.base_model import BaseModel


class City(BaseModel):
    """Handles the City class"""
    # Public class attributes
    state_id = ""
    name = ""