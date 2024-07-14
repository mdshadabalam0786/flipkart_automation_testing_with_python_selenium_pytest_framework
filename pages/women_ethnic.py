import re
from random import randint
from time import sleep
from lib.seleniumWrapper import Selenium_wrapper
from lib.xpath_women_ethnic import Xpath_women_ethnic

class Womenethnic_saree(Xpath_women_ethnic):
    def __init__(self,driver):
        self.driver=driver
    def get_women_sarees_list(self):
        count_pages = 1
        saree_brand = []
        saree_name = []
        saree_color=[]
        saree_price=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_women_ethnic.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_women_ethnic.xpathWomenEthnic)
        p1.click_element('xpath', Xpath_women_ethnic.xpathWomenSarees)
        p1.click_element('xpath',Xpath_women_ethnic.xpathSarees)
        while True:
            if count_pages != 2:
                brandElements=p1.click_elements('xpath',Xpath_women_ethnic.xpathBrands)
                for i in brandElements:
                    saree_brand.append(i.text)
                productNameElements = p1.click_elements('xpath', Xpath_women_ethnic.xpathProductNames)
                for i in productNameElements[::2]:
                    saree_name.append(i.text)
                colorElements = p1.click_elements('xpath', Xpath_women_ethnic.xpathColors)
                for i in colorElements:
                    saree_color.append(i.text)
                priceElements = p1.click_elements('xpath', Xpath_women_ethnic.xpathPrices)
                for i in priceElements:
                    price=i.text
                    price_split=''.join(price.split(','))
                    a=f"\d+"
                    filterred_price=re.findall(a, price_split)
                    if filterred_price:
                        saree_price.append(filterred_price[0])
                    else:
                        saree_price.append(price)

                p1.click_element('xpath', "//span[text()='Next']")
                self.driver.implicitly_wait(30)
                sleep(6)
                count_pages+=1
            else:
                break

        for i,j,k,l in zip(saree_brand,saree_name,saree_color,saree_price):
            print(i,j,k,l)
        sleep(5)

    def select_random_sarees_mouse_over_on_image(self):
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Womenethnic_saree.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Womenethnic_saree.xpathWomenEthnic)
        p1.click_element('xpath', Womenethnic_saree.xpathWomenSarees)
        p1.click_element('xpath', Womenethnic_saree.xpathSarees)
        priceElements = p1.click_elements('xpath', Xpath_women_ethnic.xpathPrices)
        randomNum=randint(1,40)
        priceElements[randomNum].click()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        p1.explicit_wait_by_visible_element()
        print(self.driver.title)
        p1.mouseMoveActionsToElements('xpath','//img[@class="_0DkuPH"]')
        sleep(5)

    def select_random_sarees_mouse_over_on_fullimage(self):
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Womenethnic_saree.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Womenethnic_saree.xpathWomenEthnic)
        p1.click_element('xpath', Womenethnic_saree.xpathWomenSarees)
        p1.click_element('xpath', Womenethnic_saree.xpathSarees)
        priceElements = p1.click_elements('xpath', Xpath_women_ethnic.xpathPrices)
        randomNum=randint(1,40)
        priceElements[randomNum].click()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        p1.explicit_wait_by_visible_element("xpath",'//span[@class="mEh187"]')
        p1.mouseMoveActionToFullImage('xpath','//img[@class="_0DkuPH"]')
        sleep(5)

class Women_ethnic_saree_prices_validation:
    def __init__(self,driver):
        self.driver=driver

    def validate_saree_price_range_300_to_500(self):
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Womenethnic_saree.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Womenethnic_saree.xpathWomenEthnic)
        p1.click_element('xpath', Womenethnic_saree.xpathWomenSarees)
        p1.click_element('xpath', Womenethnic_saree.xpathSarees)
        sleep(10)
