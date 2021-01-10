import pytest
import yaml
import allure
from basepage_1.page.mainpage import MainPage

with open('a.yaml') as f:
    name = yaml.safe_load(f)['dd']
    print(name)


@allure.feature('添加成员')
class Test_weixin:
    def setup(self):
        '''实例化首页'''
        self.main = MainPage()

    @pytest.mark.parametrize('name,acctid,phone', name, ids=['name_1', "name_2"])
    @allure.story('添加成员成功')
    def test_addmember(self, name, acctid, phone):
        '''首页-添加成员-保存'''
        name = self.main.go_to_addmember().addmember(name, acctid, phone).seve_addmember().address_book_list()
        print(name)
        assert '2222' in name

    @pytest.mark.parametrize('name,acctid,phone', [("狗子", 78, 15011598986)])
    @allure.story('添加成员失败')
    def test_addmenber_cancel(self, name, acctid, phone):
        '''首页-添加成员——取消-确定离开此页'''
        name_list = self.main.go_to_addmember().addmember(name, acctid, phone).cancel_addmeber().address_book_list()
        assert "狗子" not in name_list

    @pytest.mark.parametrize('name,acctid,phone', [("耗子子", 74, 15411598986), ("拉子子", 54, 13411598986)],
                             ids=["name1", "name2"])
    @allure.story('添加成员成功')
    @allure.testcase("https://www.baidu.com/", '这是一个百度连接')
    def test_address_book_goto_addmember(self, name, acctid, phone):
        '''通讯录进入添加成员保存'''
        name = self.main.go_to_address_book().go_to_addmemberpage().addmember(name, acctid,
                                                                              phone).seve_addmember().address_book_list()
        print(name)

    def test_a(self):
        print(11)
