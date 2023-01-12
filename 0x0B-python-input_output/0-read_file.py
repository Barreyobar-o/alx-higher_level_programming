#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """ Reads a file """
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            print(line, end='')
