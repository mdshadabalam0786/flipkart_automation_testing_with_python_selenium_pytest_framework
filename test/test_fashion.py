import pytest

from pages.fashion import Menstopwear
@pytest.mark.skip
def test_get_total_men_casual_shirt_list(browser):
    p1 = Menstopwear(browser)
    print(p1.get_count_men_casual_shirt_list())

def test_get_women_sarees_list(browser):

    p1 = Menstopwear(browser)
    print(p1.get_women_sarees_list())