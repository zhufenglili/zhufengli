from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_js(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID,'kw').send_keys('测试学院')
        el=self.driver.execute_script("return document.getElementById('su')")
        el.click()
        sleep(3)
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="page"]//a[last()]').click()
        sleep(5)
    def test_che(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a=document.getElementById('train_date').value='2020-3-14'")
        sleep(5)