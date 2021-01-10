import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_cookies:
    def setup_method(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_get_cookies(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db= shelve.open('./aaa/cokies')
        # db['cookie']=cookies
        # db.close()
        cookies=db['cookie']
        for i in cookies:
            self.driver.add_cookie(i)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')