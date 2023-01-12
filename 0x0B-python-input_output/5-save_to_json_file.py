#!/usr/bin/python3
""" Saves to json file """
import json


def save_to_json_file(my_obj, filename):
    """ Using json module """
    with open(filename, mode='w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
