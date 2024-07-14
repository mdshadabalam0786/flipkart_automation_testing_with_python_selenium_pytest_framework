import re
from random import randint
from time import sleep
from lib.seleniumWrapper import Selenium_wrapper
from lib.xpath_men_top_wear import Xpath_men_top_wear
class Menstopwear(Xpath_men_top_wear):
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