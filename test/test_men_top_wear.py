import pytest
from pages.men_top_wear import Mens_t_shirt,MensCasualShirt
@pytest.mark.skip
def test_get_total_men_casual_shirt_list(browser):
    p1 = MensCasualShirt(browser)
    print(p1.get_count_men_casual_shirt_list())
@pytest.mark.skip
def test_getTsirtFilteredByMen(browser):
    p1 = Mens_t_shirt(browser)
    print(p1.getTsirtFilteredByMen())
@pytest.mark.skip
def test_getTsirtFilteredByWomen(browser):
    p1 = Mens_t_shirt(browser)
    print(p1.getTsirtFilteredByWomen())
@pytest.mark.skip
def test_getTsirtFilteredInPriceRange(browser):
    p1=Mens_t_shirt(browser)
    p1.getTsirtFilteredInPriceRange("200","500")

'''testing with multiple brand'''
header="brand"
data=[("nike"),("adidas")]
@pytest.mark.parametrize(header,data)
def test_getTsirtFilteredByBrand(browser,brand):
    p1 = Mens_t_shirt(browser)
    p1.getTsirtFilteredByBrand(brand)

header="discount"
data=[("30"),("40"),("50"),("60"),("70")]
@pytest.mark.parametrize(header,data)
def test_getTsirtFilteredByDiscount(browser,discount):
    p1=Mens_t_shirt(browser)
    p1.getTsirtFilteredByDiscount(discount)

header="rateing"
data=[("3"),("4")]
@pytest.mark.parametrize(header,data)
def test_getTsirtFilteredByRating(browser,rateing):
    p1=Mens_t_shirt(browser)
    p1.getTsirtFilteredByRating(rateing)

