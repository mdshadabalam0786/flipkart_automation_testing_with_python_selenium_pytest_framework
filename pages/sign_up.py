from time import sleep
from lib.seleniumWrapper import Selenium_wrapper
class SignUp:
    def __init__(self,driver):
        self.driver=driver
    def sign_upvalid(self):
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath","//span[text()='Login']")
        p1.click_element("xpath","//span[text()='Sign Up']")
        p1.sendKey("xpath", '//input[@class="r4vIwl BV+Dqf"]', "7050327917")
        p1.click_element("xpath",'//span[text()="CONTINUE"]')
        self.driver.save_screenshot("screenshot/signup_valid.png")
        self.driver.implicitly_wait(20)
        # p1.click_element("xpath",'//span[text()="Signup"]')

    def sign_upinvalid(self):
        p1=Selenium_wrapper(self.driver)
        p1.mouseMoveActionToElement("xpath","//span[text()='Login']")
        p1.click_element("xpath","//span[text()='Sign Up']")
        p1.sendKey("xpath", '//input[@class="r4vIwl BV+Dqf"]', "alamsahdab786@gmail.com")
        p1.click_element("xpath",'//span[text()="CONTINUE"]')
        self.driver.save_screenshot("screenshot/signup_invalid.png")
        self.driver.implicitly_wait(20)


