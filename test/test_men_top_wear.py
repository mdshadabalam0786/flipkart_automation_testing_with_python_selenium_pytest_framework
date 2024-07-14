import pytest
from pages.men_top_wear import Menstopwear

def test_get_total_men_casual_shirt_list(browser):
    p1 = Menstopwear(browser)
    print(p1.get_count_men_casual_shirt_list())