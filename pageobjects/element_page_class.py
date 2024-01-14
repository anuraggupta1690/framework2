"""
element_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class ElementPage(BaseClass):
    """
    This is Page Object class for Element page
    """

    def __init__(self, driver, url: str = URLs.elements_page):
        super().__init__(driver, url)
