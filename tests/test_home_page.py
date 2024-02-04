"""
test_home_page file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""

import pytest

from lib.constants import PageTitles, PageHeaders

from lib.logging_ import get_logger as logger_

#@pytest.mark.parametrize("get_driver", [{"browser": "ff"}], indirect=True)
def test_title_home_page(get_home_page):
    """This test verify home page title"""
    logger_().info("This info from test_title_home_page")
    get_home_page.open_page()
    actual_title = get_home_page.get_title()
    assert actual_title == PageTitles.title, f"Expected Home page title is {PageTitles.title}, but found {actual_title}"


@pytest.mark.parametrize("icon", ['element', 'form', 'alert', 'widgets', 'interation', 'book'])
def test_verify_icons_are_displayed_on_home_page(get_home_page, icon):
    """This test verify all icons are present on home page"""
    # get_home_page.driver.execute_script("arguments[0].scrollIntoView();", get_home_page.get_icon(icon_name=icon))
    # get_home_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    logger_().info("This info from test_title_home_page")
    get_home_page.open_page()
    assert get_home_page.get_icon(icon_name=icon).is_displayed(), f"Failed to find {icon} on home page"


@pytest.mark.parametrize("icon", ['element', 'form', 'alert', 'widgets', 'interation', 'book'])
def test_verify_user_is_able_to_click_on_icons_which_are_displayed_on_home_page(get_home_page, icon):
    """ This test verify user is able to clicks all icons present on icon page"""
    logger_().error(f"This info from test_verify_user_is_able_to_click_on_icons_which_are_displayed_on_home_page {icon}")
    get_home_page.open_page()
    get_home_page.click_on_icon(icon_name=icon)
    actual_header = get_home_page.get_header()
    assert actual_header == getattr(PageHeaders, icon), f"Expected page header is {getattr(PageHeaders, icon)}, " \
                                                        f"but found {actual_header}"
