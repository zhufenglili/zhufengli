'''首页'''
from time import sleep

from selenium.webdriver.common.by import By

from basepage_1.page.basepage import Besepage
from basepage_1.page.addmemberpage import AddMemBerPage
from basepage_1.page.address_bookpage import Address_bookPage


class MainPage(Besepage):
    base_url=('https://work.weixin.qq.com/wework_admin/frame#index')
    _addmember=(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)')
    _address=(By.ID,'menu_contacts')
    def go_to_addmember(self):

        '''添加成员'''
        self.wait_for_click(self._addmember)
        self.send_find(*self._addmember).click()
        return AddMemBerPage(self.driver)
    def go_to_import_addressbook(self):
        '''导入通讯录'''
        pass

    def go_to_address_book(self):
        '''去通讯录'''
        self.send_find(*self._address).click()
        return Address_bookPage(self.driver)
