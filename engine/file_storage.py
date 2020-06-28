#!/usr/bin/python3
"""that serializes instances to a JSON file and deserializes JSON file to instances"""
import json

class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "json.file"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj["id"]] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(self.__file_path, mode="w+", encoding="utf-8") as File:
                string = json.dumps(self.__objects)
                File.write(string)
        except(TypeError):
            pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(self.__file_path) as json_file:
            data = json.load(json_file)
