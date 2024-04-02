"""This module contains the Base model where others inherit from"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """This is the BaseModel class that other classes inherit from"""
    # Public instance attributes
    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string repr of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    # Public instance methods
    def save(self):
        """Updates updated_at with the current date time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all key/values of the __dict__ instance"""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for key, values in self.__dict__.items():
            if key == 'created_at':
                new_dict['created_at'] = values.isoformat()
            elif key == 'updated_at':
                new_dict['updated_at'] = values.isoformat()
            else:
                new_dict[key] = values
        return new_dict
