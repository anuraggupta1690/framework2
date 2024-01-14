"""
interaction_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class InteractionPage(BaseClass):
    """
    This is Page Object class for Interaction page
    """

    def __init__(self, driver, url: str = URLs.interaction_page):
        super().__init__(driver, url)
