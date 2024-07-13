import re
from time import sleep
from lib.seleniumWrapper import Selenium_wrapper
class Menstopwear:
    xpathFashion='//div[@aria-label="Fashion"]'
    xpathMenTopWear='//a[text()="Men\'s Top Wear"]'
    xpathMenCasualShirts='//a[text()="Men\'s Casual Shirts"]'
    xpathWomenEthnic='//a[text()="Women Ethnic"]'
    xpathWomenSarees='//a[text()="Women Sarees"]'
    xpathSarees="""//a[@title="Women's Sarees"]"""
    def __init__(self,driver):
        self.driver=driver

    def get_count_men_casual_shirt_list(self):
        count_item=0
        count_pages=0
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath",Menstopwear.xpathFashion)
        p1.mouseMoveActionToElement('xpath',Menstopwear.xpathMenTopWear)
        p1.click_element('xpath',Menstopwear.xpathMenCasualShirts)
        while True:
            count_pages+=1
            elements=self.driver.find_elements('xpath','//img[@class="_53J4C-"]')
            self.driver.implicitly_wait(20)
            count_item+=len(elements)
            if count_pages!=26:
                p1.click_element('xpath',"//span[text()='Next']")
                self.driver.implicitly_wait(30)
                sleep(4)
            else:
                break

        return f"pages is :{count_pages}and total is:{count_item}"
        sleep(5)

    def get_women_sarees_list(self):
        count_pages = 1
        saree_brand = []
        saree_name = []
        saree_color=[]
        saree_price=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Menstopwear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Menstopwear.xpathWomenEthnic)
        p1.click_element('xpath', Menstopwear.xpathWomenSarees)
        p1.click_element('xpath',Menstopwear.xpathSarees)
        while True:
            if count_pages != 26:
                brandElements=self.driver.find_elements('xpath','//div[@class="syl9yP"]')
                for i in brandElements:
                    saree_brand.append(i.text)
                productNameElements = self.driver.find_elements('xpath', '//div[@class="syl9yP"]/following-sibling::a')
                for i in productNameElements[::2]:
                    saree_name.append(i.text)
                colorElements = self.driver.find_elements('xpath', '//div[@class="Br9IW+"]')
                for i in colorElements:
                    saree_color.append(i.text)
                priceElements = self.driver.find_elements('xpath', '//a[@class="+tlBoD"]')
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

        return f"Saree brand list is-----{saree_brand}{len(saree_brand)}saree name list-----{saree_name}{len(saree_name)}saree color list-------{saree_color}{len(saree_color)}saree price is-------{saree_price}{len(saree_price)}"
        sleep(5)
