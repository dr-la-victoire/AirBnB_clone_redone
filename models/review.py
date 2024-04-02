"""This is the Review module that inherits from the Base"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Handles the Review class"""
    # Public class attributes
    place_id = ""
    user_id = ""
    text = ""