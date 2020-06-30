#!/usr/bin/python3
"""that serializes instances from and to a JSON file"""
import json


class FileStorage():
    """serializes instances from and to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, mode="w+",
                      encoding="utf-8") as F:
                copy = FileStorage.__objects.copy()
                for key, value in copy.items():
                    copy[key] = value.to_dict()
                string = json.dumps(copy)
                F.write(string)
        except(TypeError):
            pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as json_file:
                dict_from_json = json.load(json_file)
                for key, value in dict_from_json.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass
