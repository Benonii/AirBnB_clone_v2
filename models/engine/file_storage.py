#!/usr/bin/python3

''' Takes care of string and retrieving all changes, presistnece. '''


import json


class FileStorage:
    ''' This class stores all created objects into a file and restores them.
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
        <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
        -> <class 'BaseModel'>
    '''

    def __init__(self):
        ''' Instantization '''
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self, cls=None):
        ''' Prints sll elements of the private attr objects '''
        Dict = self.__objects
        if cls is not None:
            for key, objct in self.__objects.items():
                if isinstance(objct, cls):
                    Dict[key] = objct

        return Dict

    def new(self, obj):
        ''' Setsj_dic in __objects the obj with key <obj class name>.id '''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        ''' Saves objects into a file specified by __file_path. '''

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
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists; otherwise, do nothing)
        '''

        # Putting these import statements in the beginning was causing issues.
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State

        filename = self.__file_path

        # Create a dictionary to map class names to their corresponding classes
        class_mapping = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_of_dicts = json.loads(f.read())

            for key, value in list_of_dicts.items():
                # Saves the class name and object id
                class_name, obj_id = key.split(".")

                # Creates an instance of each dict
                class_reference = class_mapping.get(class_name)

                if class_reference:
                    instance = class_reference(**value)
                    self.__objects[key] = instance

        except FileNotFoundError:
            # Don't do nothing if file doesn't exist
            pass

    def delete(self, obj=None):
        ''' deletes obj from __objects if it's inside '''
        if obj:
            keys_to_remove = [key for key, value in self.__objects.items()
                              if value == obj]
            for key in keys_to_remove:
                del self.__objects[key]

    def close(self):
        self.reload()
