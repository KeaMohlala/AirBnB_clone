#!/usr/bin/python3
"""
module to store objects
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """
    serializes instances to JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    # define a dictionary mapping class names to class objects
    __models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
     }

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in objects the obj with key
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes objects to JSON file
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    # use the __models dictionary to get the class object
                    if class_name in self.__models:
                        self.__objects[key] = self.__models[class_name](
                                **value
                        )

        except (FileNotFoundError, PermissionError):
            pass
