from time import sleep
from lib.seleniumWrapper import Selenium_wrapper
from selenium.webdriver.common.action_chains import ActionChains
class Login:
    def __init__(self,driver):
        self.driver=driver
    def loginInvalid(self):
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath","//span[text()='Login']")
        p1.click_element("xpath",'//li[text()="My Profile"]')
        p1.sendKey("xpath",'//input[@class="r4vIwl BV+Dqf"]',"705032791")
        p1.click_element('xpath','//button[text()="Request OTP"]')
        self.driver.save_screenshot("screenshot/logininvalid.png")
        sleep(10)
    def loginvalid(self):
        expected_title="flipkart"
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath","//span[text()='Login']")
        p1.click_element("xpath",'//li[text()="My Profile"]')
        p1.sendKey("xpath",'//input[@class="r4vIwl BV+Dqf"]',"7050327916")

        p1.click_element('xpath','//button[text()="Request OTP"]')
        self.driver.save_screenshot("screenshot/loginvalid.png")
        sleep(20)
        assert self.driver.title == expected_title, f"Title validation failed. Expected: '{expected_title}', but got: '{self.driver.title}'"


