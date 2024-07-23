import pytest
from pages.fashion.men.men_clothing.men_casual_shirts import MensCasualShirt
from pages.fashion.men.men_clothing.men_t_shirts import Mens_t_shirt

def test_get_total_men_casual_shirt_list(browser):
    p1 = MensCasualShirt(browser)
    print(p1.get_count_men_casual_shirt_list())

def test_getTsirtFilteredByMen(browser):
    p1 = Mens_t_shirt(browser)
    print(p1.getTsirtFilteredByMen())


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

"""XS,2XS,S,M,L,XL,2XL,3XL,4XL,5XL,6XL,7XL,8XL"""
header="size"
data=[("s")]
@pytest.mark.parametrize(header,data)
def test_getTsirtFilteredBySize(browser,size):
    p1=Mens_t_shirt(browser)
    p1.getTsirtFilteredBySize(size)


"""Cotton Blend,Elastane,Linen Blend,Modal,Nylon,Organic Cotton,Poly Cotton,Polyester,Pure Cotton,Viscose Rayon,Wool Blend"""
header = "fabric"
data = [("Cotton Blend")]
@pytest.mark.parametrize(header, data)
def test_getTsirtFilteredByFabric(browser, fabric):
    p1 = Mens_t_shirt(browser)
    p1.getTsirtFilteredByFabric(fabric)

"""Animal Print,Abstract,Cartoon,Checkered,Colorblock,Conversational,Embroidered,Floral Print,Geometric Print
Graphic Print,Military Camouflage,Polka Print,Printed,Self Design,Solid,Sporty,Striped,Tie & Dye,Typography"""
header = "pattern"
data = [("Abstract")]
@pytest.mark.parametrize(header, data)
def test_getTsirtFilteredByPattern(browser, pattern):
    p1 = Mens_t_shirt(browser)
    p1.getTsirtFilteredByPattern(pattern)


