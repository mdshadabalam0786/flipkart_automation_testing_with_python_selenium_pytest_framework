import pytest
from selenium import webdriver
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    