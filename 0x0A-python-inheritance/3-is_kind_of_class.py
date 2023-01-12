#!/usr/bin/python3
""" A Function """


def is_kind_of_class(obj, a_class):
    """ Checks for type """
    if isinstance(obj, a_class) is True:
        return True
    return False
