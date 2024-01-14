"""
forms_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class FormsPage(BaseClass):
    """
    This is Page Object class for Element page
    """

    def __init__(self, driver, url: str = URLs.forms_page):
        super().__init__(driver, url)
