"""
interaction_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class BooksPage(BaseClass):
    """
    This is Page Object class for Books page
    """

    def __init__(self, driver, url: str = URLs.books_page):
        super().__init__(driver, url)
