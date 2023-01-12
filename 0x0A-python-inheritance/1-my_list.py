#!/usr/bin/python3
""" A class """


class MyList(list):
    """ Inherits the list class """

    def print_sorted(self):
        """Sorts a list"""
        print(sorted(self))
