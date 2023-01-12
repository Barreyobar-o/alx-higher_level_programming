#!/usr/bin/python3
""" Inherits Base Geometry class from 7"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Init method """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculates area """
        return self.__height * self.__width

    def __str__(self):
        """ The string repr... of a rectangle """
        name = str(self.__class__.__name__)
        return "[{}] {}/{}".format(name, str(self.__width), str(self.__height))
