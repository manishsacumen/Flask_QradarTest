__author__ = 'Sacumen(www.sacumen.com)'

"""Data store module

Contains helper functions to access data store file defined in config.py
"""

import json

from config import DATA_STORE_FILE_PATH


def overwrite_data_store(data):
    """Overwrite current data file if exists otherwise creates new file and writes data

    :param data: dict
    :return: None
    """
    with open(DATA_STORE_FILE_PATH, 'w') as f:
        json.dump(data, f)


def update_data_store(data):
    """Updates current data file if available otherwise creates new file and writes data

    Uses standard dictionary update logic. ie if the key is already present, updates its value,
    Otherwise creates a new key value pair

    :param data: dict
    :return: None
    """
    try:
        with open(DATA_STORE_FILE_PATH, 'r') as f:
            current_data = json.load(f)
    except IOError:
        current_data = {}

    current_data.update(data)
    overwrite_data_store(current_data)


def read_data_store():
    """Returns all data in data file

    Reads all the data from the file and converts it into a dictionary.
    If dat file is not present, an empty dictionary will be returned

    :return: dict
    """
    try:
        with open(DATA_STORE_FILE_PATH, 'r') as f:
            return json.load(f)
    except IOError:
        return {}
