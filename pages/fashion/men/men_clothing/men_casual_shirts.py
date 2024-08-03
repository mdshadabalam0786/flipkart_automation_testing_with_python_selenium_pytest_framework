import re
from random import randint
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from lib.seleniumWrapper import Selenium_wrapper
from lib.xpath_man import Xpath_men_casual_shirt,Xpath_men_top_wear

class MensCasualShirt:
    def __init__(self,driver):
        self.driver=driver

    def get_count_men_casual_shirt_list(self):
        count_item=0
        count_pages=0
        p1=Selenium_wrapper(self.driver)
        p1.click_element("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath',Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpathMenCasualShirts1)
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

    def getCasualSirtFilteredByMen(self):
        original_product_name_list=[]
        product_name_list_filttered_only_men=[]
        product_name_=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        sleep(5)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_casual_shirt_gender)
        sleep(2)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_casual_shirt_filtter_gender_by_men)
        sleep(4)
        product_name_list_elements=p1.click_elements("xpath",Xpath_men_casual_shirt.xpath_casual_shirt_productnames)
        sleep(2)
        for product_name in product_name_list_elements[0:len(product_name_list_elements):2]:
            if "Men" in product_name.text:
                product_name_list_filttered_only_men.append(product_name.text)
            else:
                product_name_list_filttered_only_men.append("*********null**************")

        return product_name_list_filttered_only_men
        sleep(2)

    def getCasualsirtFilteredInPriceRange(self,min_price,max_price):
        t_shirt_price_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.select_drop_down_by_value("xpath",Xpath_men_casual_shirt.xpath_casual_shirt_select_min_price,min_price)
        sleep(5)
        p1.select_drop_down_by_value("xpath", Xpath_men_casual_shirt.xpath_casual_shirt_select_max_price, max_price)
        sleep(5)
        prices_list_elements=p1.click_elements("xpath",Xpath_men_casual_shirt.xpathCasualshirtPrices)
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

    def getCasualsirtFilteredByBrand(self,brand_name):
        brand_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element("xpath",Xpath_men_casual_shirt.xpath_brand)
        sleep(5)
        p1.sendKey('xpath', Xpath_men_casual_shirt.xpathSearchBrand, brand_name)
        sleep(2)
        brand_name_=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{brand_name}"]/..'
        p1.click_element("xpath",brand_name_)
        sleep(10)
        brand_list_elements=p1.click_elements("xpath",Xpath_men_casual_shirt.xpathCasualshirtBrands)
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

    def getCasualsirtFilteredByDiscount(self,discount_rate):
        discount_list=[]
        filttered_discount=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpathDiscount)
        sleep(2)
        xpath_discount=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{discount_rate}% or more"]/..'
        p1.click_element('xpath',xpath_discount)
        sleep(2)
        discount_element_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)
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

    def getCasualsirtFilteredByRating(self,rating):
        rating_list=[]
        with_rating_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        xpath_rating=f'//div[@class="XqNaEv"]/following-sibling::div[text()="{rating}★ & above"]/..'
        p1.click_element('xpath',xpath_rating)
        sleep(5)
        element_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)

        for i in element_list:
            parent_window = self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath','(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])

            try:
                # Attempt to find the element
                element = self.driver.find_element('xpath', '//div[@class="XQDdHH _1Quie7"]')

                # Check if the element is visible and append its text if it is
                if element.is_displayed():
                    rating_list.append(element.text)
                else:
                    print("Element is not visible, skipping this element.")
            except NoSuchElementException:
                # Handle the case where the element is not found
                with_rating_list.append("Element not found, skipping this element.")
            finally:
                # Close the current window and switch back to the parent window
                self.driver.close()
                self.driver.switch_to.window(parent_window)

        print(rating_list)
        print(with_rating_list)
        for j in rating_list:
            if not j>=rating:
                print("rating is not working according to filttered")
                break
        else:
            print("rating is working according to filttered")

    def getCasualsirtFilteredBySize(self,size):
        with_size_list=[]
        p1 = Selenium_wrapper(self.driver)
        p1.click_element("xpath", Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpathSize)
        size_=size.upper()
        p1.click_element('xpath',f'//div[@class="XqNaEv"]/following-sibling::div[text()="{size_}"]/..')
        sleep(3)
        element_list = p1.click_elements('xpath', Xpath_men_casual_shirt.xpathCasualshirtPrices)
        for i in element_list:
            parent_window = self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath', '(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            size_elements=p1.click_elements('xpath','//span[@id="Size"]/..//li')
            sleep(2)
            size_list=[]
            for i in range(0,len(size_elements)-1,1):
                size_list.append(size_elements[i].text)
            with_size_list.append(size_list)
            self.driver.close()
            self.driver.switch_to.window(parent_window)

        for i in with_size_list:
            if not size_ in i:
                print("size filltered is not working")
                break
        else:
            print(with_size_list)

    def getCasualsirtFilteredByFabric(self,fabric):
        list_of_brand_name=[]
        p1=Selenium_wrapper(self.driver)
        p1.click_element("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_fabric)
        sleep(3)
        fabric_xpath=f'//div[text()="{fabric}"]/..'
        p1.click_element('xpath',fabric_xpath)
        sleep(3)
        elements_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)
        for i in elements_list:
            parent_window=self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath', '(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            element_brandName=self.driver.find_element("xpath",'//span[@class="VU-ZEz"]')
            self.driver.implicitly_wait(20)
            list_of_brand_name.append(element_brandName.text)
            self.driver.close()
            self.driver.switch_to.window(parent_window)

        for i in list_of_brand_name:
            if not fabric in i:
                print(f"fabric filter is not working as expected {fabric}")
                break
        else:
            print(list_of_brand_name)

    def getCasualsirtFilteredByPattern(self,pattern):
        list_of_brand_name=[]
        p1=Selenium_wrapper(self.driver)
        p1.click_element("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_pattern)
        sleep(3)
        p1.click_element('xpath','//div[@class="e+xvXX KvHRYS"]//span[text()="12 MORE"]')
        sleep(2)
        fabric_xpath=f'//div[text()="{pattern}"]/..'
        p1.click_element('xpath',fabric_xpath)
        sleep(3)
        elements_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)
        for i in elements_list:
            parent_window=self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath', '(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            element_brandName=self.driver.find_element("xpath",'//span[@class="VU-ZEz"]')
            self.driver.implicitly_wait(20)
            list_of_brand_name.append(element_brandName.text)
            self.driver.close()
            sleep(1)
            self.driver.switch_to.window(parent_window)

        for i in list_of_brand_name:
            if not pattern in i:
                print(list_of_brand_name)
                print(f"pattern filter is not working as expected {pattern}")
                break
        else:
            print(list_of_brand_name)

    def getCasualsirtFilteredByColor(self,color):
        list_of_brand_name=[]
        p1=Selenium_wrapper(self.driver)
        p1.click_element("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_color)
        sleep(3)

        fabric_xpath=f'//div[text()="{color}"]/..'
        p1.click_element('xpath',fabric_xpath)
        sleep(3)
        elements_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)
        for i in elements_list:
            parent_window=self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath', '(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            element_brandName=self.driver.find_element("xpath",'//span[@class="VU-ZEz"]')
            self.driver.implicitly_wait(20)
            list_of_brand_name.append(element_brandName.text)
            self.driver.close()
            sleep(1)
            self.driver.switch_to.window(parent_window)

        for i in list_of_brand_name:
            if not color in i:
                print(list_of_brand_name)
                print(f"pattern filter is not working as expected {color}")
                break
        else:
            print(list_of_brand_name)


    def getCasualsirtFilteredByPackOf(self,pack_of):
        list_of_brand_name=[]
        p1=Selenium_wrapper(self.driver)
        p1.click_element("xpath",Xpath_men_top_wear.xpathFashion)
        p1.mouseMoveActionToElement('xpath', Xpath_men_top_wear.xpathMenTopWear1)
        p1.click_element('xpath', Xpath_men_casual_shirt.xpathMenCasualShirts1)
        p1.click_element('xpath',Xpath_men_casual_shirt.xpath_pack_of)
        sleep(3)
        pack_of_xpath=f'//div[text()="{pack_of}"]/..'
        p1.click_element('xpath',pack_of_xpath)
        sleep(3)
        elements_list=p1.click_elements('xpath',Xpath_men_casual_shirt.xpathCasualshirtPrices)
        for i in elements_list:
            parent_window=self.driver.current_window_handle
            i.click()
            p1.explicit_wait_by_visible_element('xpath', '(//div[@class="hl05eU"])[1]')
            sleep(2)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            element_brandName=self.driver.find_element("xpath",'//span[@class="VU-ZEz"]')
            self.driver.implicitly_wait(20)
            list_of_brand_name.append(element_brandName.text)
            self.driver.close()
            sleep(1)
            self.driver.switch_to.window(parent_window)
            sleep(1)

        for item in list_of_brand_name:
            # Extract the number of packs from the string
            num_packs = int(item.split(' ')[2])

            # Check the range and if the number of packs matches
            if pack_of == "3 - 6" and num_packs not in range(3, 7):
                print(list_of_brand_name)
                print(f"Pattern filter is not working as expected for {pack_of}")
                break
            elif pack_of == "7 - 10" and num_packs not in range(7, 11):
                print(list_of_brand_name)
                print(f"Pack of filter is not working as expected for {pack_of}")
                break
            elif pack_of == "Pack of 2" or pack_of == "Pack of 1":
                print(list_of_brand_name)
                print(f"Pack of filter is not working as expected for {pack_of}")
                break
        else:
            print(list_of_brand_name)
            print(f"All items match the filter for {pack_of}")




















