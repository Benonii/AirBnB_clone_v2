#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            Dict = FileStorage.__objects
            for objct in Dict:
                i = 0
                if type(objct) == cls:
                    Dict[i] = objct
                    i = i + 1
            return Dict

        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""

        filename = self.__file_path
        # Saves the data that will be written to the file
        data_to_write = {}

        for key, obj in self.__objects.items():
            # Converts each object in __objects to a dict
            obj_dict = obj.to_dict()

            # Filter empty keys
            filtered_dict = {k: v for k, v in obj_dict.items() if v}

            if filtered_dict:
                data_to_write[key] = filtered_dict

        with open(filename, "w", encoding="utf-8") as f:
            # Writes the dict to file.json
            json.dump(data_to_write, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' Deletes object from __objects if it's inside.
            Does nothing if obj is None '''

        if obj is not None:
            Dict = FileStorage.__objects
            for key, objct in Dict.items():
                if objct == obj:
                    del Dict[key]
                    break
