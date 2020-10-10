import requests
import pytest


class Test_tagname:
    def setup_class(self):
        '''定义token'''
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4lSuF3ZiIuJt9qFqQ5-MMkw"
        access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        self.tagid = 2
        parm = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(url=access_token, params=parm)
        self.token = r.json()["access_token"]

    def test_creat_tagname(self):
        '''创建标签'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {

            "tagname": "第一个标签",
            "tagid": self.tagid

        }
        r = requests.post(url=url, json=data)
        print(r.json())

        list = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r_list = requests.get(url=list)
        print(r_list.json())
        # 断言列表的第一个标签
        assert r_list.json()["taglist"][0]["tagname"] == '第一个标签'

    def test_updat_tagname(self):
        '''更新标签'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": self.tagid,
            "tagname": "更改标签"
        }
        r = requests.post(url=url,json=data)
        print(r.json())
        #获取列表标签
        list = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r_list = requests.get(url=list)
        print(r_list.json())
        # 断言列表的第一个标签
        assert r_list.json()["taglist"][0]["tagname"] == '更改标签'

    def test_del_tagname(self):
        '''删除接口'''

        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={self.tagid}"
        r = requests.get(url=url)
        print(r.json())
        # 获取标签列表
        list = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r_list = requests.get(url=list)
        print(r_list.json())
