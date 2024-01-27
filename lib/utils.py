"""
utils file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""
import json

from path import get_project_path


def read_test_data_file(file_path: str) -> dict:
    """
    Function which return json file data into dict format
    :param str file_path: Json File path of
    :return: dict of Json file
    :rtype: dict
    """
    with open(get_project_path() + file_path) as json_file:
        data = json.load(json_file)
    return data

