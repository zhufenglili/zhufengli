from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Besepage:
    base_url = ""

    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)




        else:
            self.driver: WebDriver = driver_base
        if self.base_url != "":
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)


    def send_find(self, by, value):
        return self.driver.find_element(by, value)

    def sen_finds(self, by, value):
        return self.driver.find_elements(by, value)
    def wait_for_click(self,element):
        return WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
