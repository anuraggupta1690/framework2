"""
path.py file Designed by Anurag Gupta
 :date:  27-01-2024
 :author: Anurag Gupta
"""

import os


def get_project_path():
    """Returns root directory PAth"""
    return os.path.dirname(os.path.realpath(__file__))
