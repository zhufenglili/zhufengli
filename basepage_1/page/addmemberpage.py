from time import sleep

from selenium.webdriver.common.by import By

from basepage_1.page.basepage import Besepage
from basepage_1.page.address_bookpage import Address_bookPage

'''添加成员'''


class AddMemBerPage(Besepage):
    _username = (By.ID, 'username')
    _acctid = (By.ID, 'memberAdd_acctid')
    _phon = (By.ID, 'memberAdd_phone')
    _seve = (By.XPATH, '//*[@class="member_colRight_operationBar ww_operationBar"]//a[2]')
    _cancel = (By.XPATH, '//*[@class="member_colRight_operationBar ww_operationBar"]//a[3]')

    _cancel_1=(By.XPATH,'//*[@class="qui_dialog_foot ww_dialog_foot"]//a[2]')

    def addmember(self, name, acctid, phone):
        '''添加成员页'''
        self.wait_for_click(self._username)
        self.send_find(*self._username).send_keys(name)
        self.send_find(*self._acctid).send_keys(acctid)
        self.send_find(*self._phon).send_keys(phone)

        return self

    def seve_addmember(self):
        '''保存添加成员'''
        self.wait_for_click(self._seve)
        self.driver.execute_script('document.documentElement.scrollTop=1000')
        self.send_find(*self._seve).click()
        return Address_bookPage(self.driver)  # 返回通讯录

    def cancel_addmeber(self):
        '''取消保存添加成员'''
        self.send_find(*self._cancel).click()
        self.wait_for_click(self._cancel_1)
        self.send_find(*self._cancel_1).click()
        return Address_bookPage(self.driver)  # 返回通讯录
