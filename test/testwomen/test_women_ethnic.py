import pytest
from pages.fashion.women.women_ethnic.women_sarees import Womenethnic_saree
from pages.fashion.women.women_ethnic.women_sarees import Women_ethnic_saree_prices_validation


def test_get_women_sarees_list(browser):
    p1 = Womenethnic_saree(browser)
    p1.get_women_sarees_list()

def test_select_random_sarees_mouse_over_on_image(browser):
    p1 = Womenethnic_saree(browser)
    p1.select_random_sarees_mouse_over_on_image()

def test_select_random_sarees_mouse_over_on_fullimage(browser):
    p1 = Womenethnic_saree(browser)
    p1.select_random_sarees_mouse_over_on_fullimage()

def test_validate_saree_price_range_300_to_500(browser):
    p1=Women_ethnic_saree_prices_validation(browser)
    p1.validate_saree_price_range_300_to_500()
