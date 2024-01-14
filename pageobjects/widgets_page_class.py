"""
widgets_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class WidgetsPage(BaseClass):
    """
    This is Page Object class for Widgets page
    """

    def __init__(self, driver, url: str = URLs.widgets_page):
        super().__init__(driver, url)
