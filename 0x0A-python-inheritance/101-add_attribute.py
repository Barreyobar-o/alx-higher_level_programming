#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """_summary_

    Args:
        obj (_type_): _description_
        att (_type_): _description_
        value (_type_): _description_

    Raises:
        TypeError: _description_
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
