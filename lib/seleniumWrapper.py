from selenium.webdriver.common.action_chains import ActionChains
class Selenium_wrapper:
    def __init__(self,driver):
        self.driver=driver
    def click_element(self,*args):
        self.driver.find_element(f"{args[0]}",f"{args[1]}").click()
        self.driver.implicitly_wait(20)
    def sendKey(self,*args):
        self.driver.find_element(f"{args[0]}",f"{args[1]}").send_keys(f"{args[2]}")
        self.driver.implicitly_wait(20)

    def mouseMoveActionToElement(self,*args):
        element = self.driver.find_element(f"{args[0]}",f"{args[1]}")
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        self.driver.implicitly_wait(20)