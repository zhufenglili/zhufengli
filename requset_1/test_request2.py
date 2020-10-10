import requests


class TestReqest:
    def setup(self):
        '''
        获取token
        '''
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4vgTL5JVusjH9gxJgJCP2Xk"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.json())
        self.token = r.json()["access_token"]

    def test_1(self):
        '''创建部门'''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        param= {
            "access_token": self.token
        }
        data = {
            "name": "测试部门",
            "name_en": "JISU",
            "parentid": 2,
            "order": 3,
            "id":4
        }
        r = requests.post(url=url, json=data, params=param)
        print(r.json())
        assert r.json()["errcode"] == 48002
