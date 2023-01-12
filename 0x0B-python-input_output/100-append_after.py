#!/usr/bin/python3
""" Defines a function: append_after """


def append_after(filename="", search_string="", new_string=""):
    """ appends text to a file """
    new_text = ""
    with open(filename) as fp:
        for line in fp:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, mode="w") as file:
        file.write(new_text)
