from time import  sleep
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
class Selenium_wrapper:
    def __init__(self,driver):
        self.driver=driver
    def click_element(self,*args):
        self.driver.find_element(f"{args[0]}",f"{args[1]}").click()
        self.driver.implicitly_wait(20)

    def click_elements(self,*args):
        li=self.driver.find_elements(f"{args[0]}",f"{args[1]}")
        self.driver.implicitly_wait(20)
        return li
    def sendKey(self,*args):
        self.driver.find_element(f"{args[0]}",f"{args[1]}").send_keys(f"{args[2]}")
        self.driver.implicitly_wait(20)
    def explicit_wait_by_visible_element(self,*args):
        wait=WebDriverWait(self.driver,20)
        wait.until(Ec.visibility_of_element_located((args[0],args[1])))

    def mouseMoveActionToElement(self,*args):
        element = self.driver.find_element(f"{args[0]}",f"{args[1]}")
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        self.driver.implicitly_wait(20)

    def mouseMoveActionToFullImage(self,*args):
        elements = self.driver.find_elements(f"{args[0]}", f"{args[1]}")
        element1 = self.driver.find_element("xpath", '//div[@class="jiOzM4"]')
        self.driver.implicitly_wait(10)
        if len(elements) >= 1:
            for element in elements:
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
                self.driver.implicitly_wait(20)
                action.move_to_element(element1).perform()
                self.driver.implicitly_wait(20)

                # action.move_by_offset(0, 10).perform()
                self.driver.execute_script("window.scrollBy(0, 100);")

                sleep(3)
                a = datetime.now().second
                self.driver.save_screenshot(f"screenshot/screenshot_saree_img1/saree_img{a}.png")
                sleep(4)

    def mouseMoveActionsToElements(self,*args):
        elements = self.driver.find_elements(f"{args[0]}",f"{args[1]}")
        self.driver.implicitly_wait(10)
        if len(elements)>=1:
            for element in elements:
                action = ActionChains(self.driver)
                action.move_to_element(element).perform()
                self.driver.implicitly_wait(20)
                a=datetime.now().second
                self.driver.save_screenshot(f"screenshot/screenshot_saree_img/saree_img{a}.png")
                sleep(4)


