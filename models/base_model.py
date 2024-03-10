#!/usr/bin/python3
"""
module that defines a base class
which all other classes well inherit from
"""
import datetime
import uuid
import models


class BaseModel:
    """
    documentation for class 'BaseModel'
    """
    def __init__(self, *args, **kwargs):
        """
        every instance will be initialized with a unique id
        and datetime when instance was created if kwargs are empty

        the init method dynamically sets all attributes passed in kwargs
        excluding(__class__) and converts the string representations
        of datetime objects back to date time objects
        """
        if len(kwargs) == 0:
            self.id = uuid.uuid4().hex
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                # ignore the '__class__' key
                if key == "__class__":
                    continue
                elif key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    setattr(
                            self, key, datetime.datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
                else:
                    setattr(self, key, value)

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
        models.storage.save()

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
