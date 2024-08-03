import pytest
from pages.fashion.men.men_clothing.men_casual_shirts import MensCasualShirt


def test_get_total_men_casual_shirt_list(browser):
    p1 = MensCasualShirt(browser)
    print(p1.get_count_men_casual_shirt_list())

def test_getCasualSirtFilteredByMen(browser):
    p1 = MensCasualShirt(browser)
    print(p1.getCasualSirtFilteredByMen())
def test_getCasualsirtFilteredInPriceRange(browser):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredInPriceRange("250", "500")

'''testing with multiple brand'''
header="brand"
data=[("Dennis Lingo"),("The Indian Garage Co.")]
@pytest.mark.parametrize(header,data)
def test_getCasualsirtFilteredByBrand(browser,brand):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByBrand(brand)


header="discount"
data=[("30"),("40"),("50"),("60"),("70")]
@pytest.mark.parametrize(header,data)
def test_getCasualsirtFilteredByDiscount(browser,discount):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByDiscount(discount)


header="rateing"
data=[("3"),("4")]
@pytest.mark.parametrize(header,data)
def test_getCasualsirtFilteredByRating(browser,rateing):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByRating(rateing)


"""XS,2XS,S,M,L,XL,2XL,3XL,4XL,5XL,6XL,7XL,8XL"""
header="size"
data=[("s")]
@pytest.mark.parametrize(header,data)
def test_getCasualsirtFilteredBySize(browser,size):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredBySize(size)

"""Cotton Blend,Elastane,Linen Blend,Modal,Nylon,Organic Cotton,Poly Cotton,Polyester,Pure Cotton,Viscose Rayon,Wool Blend"""
header = "fabric"
data = [("Cotton Blend")]
@pytest.mark.parametrize(header, data)
def test_getCasualsirtFilteredByFabric(browser, fabric):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByFabric(fabric)


"""Animal Print,Checkered,Color Block,Dyed/Ombre,Embellished,Embroidered,Ethnic Motifs.Floral Print,Geometric Print,
Graphic Print,Military Camouflage,Polka Print,Printed,Self Design,Solid,Striped,Washed,Woven Design"""
header = "pattern"
data = [("Animal Print")]
@pytest.mark.parametrize(header, data)
def test_getCasualsirtFilteredByPattern(browser, pattern):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByPattern(pattern)

"""Black,Beige,Blue,Brown,Dark Blue,Dark Green"""
header = "color"
data = [("Blue")]
@pytest.mark.parametrize(header, data)
def test_getCasualsirtFilteredByColor(browser, color):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByColor(color)



"""3 - 6,7 - 10,Pack of 2,Pack of 1"""
header = "pack_of"
data = [("7 - 10"),("Pack of 1"),("3 - 6"),("Pack of 2")]
@pytest.mark.parametrize(header, data)
def test_getCasualsirtFilteredByPackOf(browser, pack_of):
    p1 = MensCasualShirt(browser)
    p1.getCasualsirtFilteredByPackOf(pack_of)
"""================================================================="""

