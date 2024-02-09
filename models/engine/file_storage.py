#!/usr/bin/python3
"""
    File Storage Module:
    To serialize and deserialize an instance/JSON file
"""

import json
import os


class FileStorage:
    """class to serialize an instance and deserialize a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method to return dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """method to set object"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        instances = {}

        for key, value in FileStorage.__objects.items():
            instances[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(instances, f)

    def reload(self):
        """Deserializes a JSON file to an object"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        dictionary = {'BaseModel': BaseModel, 'City': City, 'Amenity': Amenity,
                      'Place': Place, 'Review': Review, 'State': State}

            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    for key, value in json.load(f).items():
                        self.new(dictionary[value[__class__]](**value))