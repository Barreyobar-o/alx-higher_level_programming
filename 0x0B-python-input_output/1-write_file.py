#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """ writes to a file """
    with open(filename, mode='w', encoding='utf-8') as fp:
        return fp.write(text)
