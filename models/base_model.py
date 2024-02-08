#!/usr/bin/python3
"""
    THIS FILE CONTAINS THE BASE MODEL CLASS
    FROM WHICH ALL OTHER CLASS IN THIS PROGRAM
    INHERITS FROM

"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represent the base class"""

    def __init__(self, *args, **kwargs):
        """Initializes the an instance of BaseModel"""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    try:
                        value = datetime.strptime(str(value), date_format)
                    except ValueError:
                        pass
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of the instance"""
        attributes = self.__dict__.copy()
        attributes["__class__"] = type(self).__name__

        for key, value in attributes.items():
            if isinstance(value, datetime):
                attributes[key] = value.isoformat()

        return attributes

    def __str__(self):
        """Returns the string representation of the instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"""
