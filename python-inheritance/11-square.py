#!/usr/bin/python3
""" task 10 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
