import re
from random import randint
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from lib.seleniumWrapper import Selenium_wrapper
from lib.xpath_men_top_wear import Xpath_men_casual_shirt,Xpath_men_t_shirt,Xpath_men_top_wear

class MensCasualShirt:
    def __init__(self,driver):
        self.driver=driver

    def get_count_men_casual_shirt_list(self):
        count_item=0
        count_pages=0
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath',Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpathMenCasualShirts)
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

class Mens_t_shirt:
    def __init__(self,driver):
        self.driver=driver
    def getTsirtFilteredByMen(self):
        original_product_name_list=[]
        product_name_list_filttered_only_men=[]
        product_name_=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        p1.click_element('xpath',Xpath_men_t_shirt.xpath_t_shirt_gender)
        p1.click_element('xpath',Xpath_men_t_shirt.xpath_t_shirt_filtter_gender_by_men)
        sleep(4)
        product_name_list_elements=p1.click_elements("xpath",Xpath_men_t_shirt.xpath_t_shirt_productnames)
        sleep(2)
        for product_name in product_name_list_elements[0:len(product_name_list_elements):2]:
            if "Men" in product_name.text:
                product_name_list_filttered_only_men.append(product_name.text)
            else:
                product_name_list_filttered_only_men.append("*********null**************")

        return product_name_list_filttered_only_men
        sleep(2)

    def getTsirtFilteredByWomen(self):
        original_product_name_list=[]
        product_name_list_filttered_only_men=[]
        product_name_=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        p1.click_element('xpath',Xpath_men_t_shirt.xpath_t_shirt_gender)
        p1.click_element('xpath',Xpath_men_t_shirt.xpath_t_shirt_filtter_gender_by_women)
        sleep(4)
        product_name_list_elements=p1.click_elements("xpath",Xpath_men_t_shirt.xpath_t_shirt_productnames)
        sleep(2)
        for product_name in product_name_list_elements[0:len(product_name_list_elements):2]:
            if "Women" in product_name.text:
                product_name_list_filttered_only_men.append(product_name.text)
            else:
                product_name_list_filttered_only_men.append("*********null**************")

        return product_name_list_filttered_only_men
        sleep(2)

    def getTsirtFilteredInPriceRange(self,min_price,max_price):
        t_shirt_price_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        p1.select_drop_down_by_value("xpath",Xpath_men_t_shirt.xpath_t_shirt_select_min_price,min_price)
        sleep(5)
        p1.select_drop_down_by_value("xpath", Xpath_men_t_shirt.xpath_t_shirt_select_max_price, max_price)
        sleep(5)
        prices_list_elements=p1.click_elements("xpath",Xpath_men_t_shirt.xpathTshirtPrices)
        for _ in prices_list_elements:
            price=_.text
            price_split = ''.join(price.split(','))
            a = f"\d+"

            filterred_price = re.findall(a, price_split)
            if filterred_price:
                t_shirt_price_list.append(filterred_price[0])
            else:
                t_shirt_price_list.append(price)

        print(t_shirt_price_list)
        for price_ in t_shirt_price_list:
            if not (int(min_price) <= int(price_) <= int(max_price)):
                print("This price is not in the range between 300 to 500:", price_)
                break
        else:
            print(f"All prices are in the range between {min_price} to {max_price}")

    def getTsirtFilteredByBrand(self,brand_name):
        brand_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        p1.click_element("xpath",Xpath_men_t_shirt.xpath_brand)
        sleep(5)
        brand_name_=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{brand_name.upper()}"]/..'
        p1.click_element("xpath",brand_name_)
        sleep(10)
        brand_list_elements=p1.click_elements("xpath",Xpath_men_t_shirt.xpathTshirtBrands)
        sleep(2)
        for i in brand_list_elements:
            brand_list.append(i.text)
        for _ in brand_list:
            brand=brand_name.upper()
            if not _==brand:
                print(brand,"is not fetchting the all same brand..")
                break
        else:
            print("it is fetchting the all same brand..")

        print(brand_list)

    def getTsirtFilteredByDiscount(self,discount_rate):
        discount_list=[]
        filttered_discount=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        p1.click_element('xpath',Xpath_men_t_shirt.xpathDiscount)
        sleep(2)
        xpath_discount=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{discount_rate}% or more"]/..'
        p1.click_element('xpath',xpath_discount)
        sleep(2)
        discount_element_list=p1.click_elements('xpath',Xpath_men_t_shirt.xpathTshirtPrices)
        sleep(2)
        for i in discount_element_list:
            discount_list.append(i.text) #here adding all 40 discount into the list

        for i in range(len(discount_list)): #here filttering only discount from price list
            split = discount_list[i].split()[0]
            matches = ''.join(re.findall('(\d{2})%', split))
            filttered_discount.append(matches)
        for dis_ in filttered_discount:
            if not dis_>=discount_rate:
                print("discount filter is not correctly working or fatching the result on user interface")
                break
        else:
            print("discount filter is correctly working or fatching the result on user interface")
            print(filttered_discount)
        sleep(5)

    def getTsirtFilteredByRating(self,rating):
        rating_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear)
        p1.click_element('xpath', Xpath_men_t_shirt.xpathMenT_Shirts)
        xpath_rating=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{rating}★ & above"]/..'
        p1.click_element('xpath',xpath_rating)
        sleep(5)
        element_list=p1.click_elements('xpath',Xpath_men_t_shirt.xpathTshirtPrices)

        for i in element_list:
            parent_window = self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath','(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            try:
                element=self.driver.find_element('xpath','//div[@class="XQDdHH _1Quie7"]')
                rating_list.append(element.text)
                self.driver.close()
                self.driver.switch_to.window(parent_window)
            except NoSuchElementException:
                print("Element not found, skipping this element.")
                continue  # Skip this element and continue with the next one
                

        print(rating_list)
        for j in rating_list:
            if not j>=rating:
                print("rating is not working according to filttered")
                break
        else:
            print("rating is working according to filttered")








        












