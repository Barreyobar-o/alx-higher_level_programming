#!/usr/bin/python3
""" append_write function """


def append_write(filename="", text=""):
    """ appends text to a file """
    with open(filename, mode='a', encoding='utf-8') as fp:
        return fp.write(text)
