import requests


class TestRequest:
    def setup(self):
        '''获取token'''
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4lSuF3ZiIuJt9qFqQ5-MMkw"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        self.id = 3

        params = {
            "corpid": corpid,
            "corpsecret": corpsecret

        }

        r = requests.get(url=url, params=params)

        self.token = r.json()["access_token"]
        print(r.json())

    def test_1(self):
        '''添加部门'''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        param = {

            "access_token": self.token

        }
        data = {
            "name": "宣传部门",
            "name_en": "jdk",
            "parentid": 1,
            "order": 9,
            "id": self.id
        }

        r = requests.post(url=url, json=data, params=param)
        print(r.json())
        assert r.json()["errcode"] == 0

    def test_update(self):
        '''更新部门名称'''
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data ={
            "id": self.id,
            "name": "广州研发中心",
            "name_en": "jdk",
            "parentid": 1,
            "order": 9
        }
        r=requests.post(url=update_url,json=data)
        list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=list_url)
        assert list.json()["department"][1]["name"] == '广州研发中心'
    def test_dele(self):
        '''删除部门'''
        url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}"
        r = requests.get(url=url)
        list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=list_url)
        assert len(list.json()["department"]) == 1

