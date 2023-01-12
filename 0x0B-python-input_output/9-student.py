#!/usr/bin/python3
""" New class: Student """


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """ Init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary description """
        return self.__dict__
