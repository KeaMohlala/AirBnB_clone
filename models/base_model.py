#!/usr/bin/python3
"""
module that defines a base class
which all other classes well inherit from
"""
import datetime
import uuid


class BaseModel:
    """
    documentation for class 'BaseModel'
    """
    def __init__(self):
        """
        every instance will be initialized with a unique id
        and datetime when instance was created
        """
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        returns string representation of a Base instance
        """
        return (
                "[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__)
        )

    def save(self):
        """
        updates 'updated_at' with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary with the key/values of __dict__ of the instance

        created_at and updated_at must be converted
        to string object in ISO format
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
