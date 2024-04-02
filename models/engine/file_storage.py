"""This module handles storing the objects to a file for persistence"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """This class handles data persistence with JSON"""
    __file_path = "file.json"
    __objects = {}

    # Public instance methods
    def all(self):
        """Returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj in the objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the objects dictionary to the JSON file"""
        # creating a new dictionary to store the instances
        new_dict = {}
        # iterating over the objects in the __objects dictionary
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as j_file:
            json.dump(new_dict, j_file)

    def reload(self):
        """Deserializes the JSON file to __objects dictionary"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
            }

        try:
            if not os.path.exists(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, encoding="utf-8") as j_str:
                the_dict = json.load(j_str)
            # Getting the values of the keys in the the_dict dictionary
            for value in the_dict.values():
                class_name = value["__class__"]
                class_obj = classes[class_name]
                self.new(class_obj(**value))
        except FileNotFoundError:
            pass
