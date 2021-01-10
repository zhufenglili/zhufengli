from time import sleep

from selenium.webdriver.common.by import By

from basepage_1.page.basepage import Besepage

'''通讯录'''


class Address_bookPage(Besepage):
    _listaddress = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
    _addmenber = (By.XPATH, "//*[@class='ww_operationBar']//a[1]")

    def address_book_list(self):
        '''通讯录列表'''
        self.wait_for_click(self._listaddress)
        list_address = self.sen_finds(*self._listaddress)
        return [i.text for i in list_address]

    def go_to_addmemberpage(self):
        '''添加成员'''
        from basepage_1.page.addmemberpage import AddMemBerPage
        self.wait_for_click(self._addmenber)
        self.send_find(*self._addmenber).click()
        return AddMemBerPage(self.driver)
