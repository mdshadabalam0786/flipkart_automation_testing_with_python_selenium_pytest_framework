class Xpath_men_top_wear:
    xpathFashion = '//div[@aria-label="Fashion"]'
    xpathMenTopWear = '//a[text()="Men\'s Top Wear"]'


class Xpath_men_casual_shirt:
    xpathMenCasualShirts = '//a[text()="Men\'s Casual Shirts"]'

class Xpath_men_t_shirt:
    xpathMenT_Shirts = '//a[text()="Men\'s T-Shirts"]'
    xpath_t_shirt_gender="//div[text()='Gender']/.."
    xpath_t_shirt_filtter_gender_by_men='//div[@class="XqNaEv"]/following-sibling::div[text()="Men"]'
    xpath_t_shirt_filtter_gender_by_women = '//div[@class="XqNaEv"]/following-sibling::div[text()="Women"]'
    xpath_t_shirt_productnames = '//div[@class="syl9yP"]/following-sibling::a'
    xpath_t_shirt_select_min_price='(//select[@class="Gn+jFg"])[1]'
    xpath_t_shirt_select_max_price='(//select[@class="Gn+jFg"])[2]'
    xpathTshirtPrices = '//a[@class="+tlBoD"]'
    xpathTshirtBrands = '//div[@class="syl9yP"]'
    xpath_brand='//div[text()="Brand"]'
    xpathDiscount='//div[text()="Discount"]'
    xpathRating='//div[text()="Customer Ratings"]'