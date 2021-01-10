from time import sleep

from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_a:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_a(self):
        self.driver.get('https://www.baidu.com/')
        action=ActionChains(self.driver)
        a= self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]//a[2]')
        action.click(a)
        action.double_click(a)
        action.perform()
        sleep(4)