#!/usr/bin/python3
""" classes """
import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
