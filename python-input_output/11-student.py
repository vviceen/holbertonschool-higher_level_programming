#!/usr/bin/python3
""" task 11 """


class Student:
    """ defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance """
        for attr in json:
            if hasattr(self, attr):
                setattr(self, attr, json[attr])
