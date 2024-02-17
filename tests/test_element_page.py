"""
test_element_page file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""

import pytest

from lib.constants import PageTitles, PageHeaders
from lib.logging_ import get_logger as logger_
from lib.utils import read_test_data_file
TEST_FILE = read_test_data_file(r"\test_data\test_element_page.json")


def test_verify_user_is_able_to_fill_the_form(get_element_page):
    logger_().info("test_verify_user_is_able_to_fill_the_form started ")
    expected_values = TEST_FILE["user_details"]
    get_element_page.open_page()
    logger_().info("Element page opened")
    get_element_page.text_box_click()
    get_element_page.enter_full_name(expected_values["name"])
    get_element_page.enter_email(expected_values["email"])
    get_element_page.enter_current_address(expected_values["current_address"])
    get_element_page.enter_permanent_address(expected_values["permanent_address"])
    get_element_page.submit()
    logger_().info("Element page submit button clicked")
    for element, values in expected_values.items():
        actual_value = get_element_page.get_text_value(element=element).split(":")[1]
        try:
            assert actual_value == values, f"Expected value for {element} is {values}, but found {actual_value}"
        except AssertionError as ae:
            logger_().error(f"test_verify_user_is_able_to_fill_the_form Exception: {ae}")
        logger_().info(f"test_verify_user_is_able_to_fill_the_form completed")


def test_click_check_box(get_element_page):
    logger_().info("test_click_check_box started")
    get_element_page.open_page()
    logger_().info("Element page opened")
    get_element_page.click_check_box()
    logger_().info("clicked on Element page check box")
    try:
        assert get_element_page.get_check_box_result_text() == TEST_FILE["check_box_result"]
    except AssertionError as ae:
        logger_().error(f"test_click_check_box Exception: {ae}")
    logger_().info("test_click_check_box completed")
