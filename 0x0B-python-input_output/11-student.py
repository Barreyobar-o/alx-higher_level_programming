#!/usr/bin/python3
"""Defines Student class """


class Student:
    """Student class """

    def __init__(self, first_name, last_name, age):
        """ Init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dictionary description """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Changes attribtes of the Student class """
        for i, j in json.items():
            setattr(self, i, j)
