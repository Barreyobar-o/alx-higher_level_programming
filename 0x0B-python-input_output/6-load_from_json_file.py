#!/usr/bin/python3
""" Load from json file """
import json


def load_from_json_file(filename):
    """ Using json module """
    with open(filename) as fp:
        return json.load(fp)
