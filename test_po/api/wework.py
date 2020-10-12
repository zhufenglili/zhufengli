import requests

from test_po.api.baseapi import Baseapi


class Wework(Baseapi):
    '''token'''
    def get_token(self,corpsecret):
        '''定义token'''
        corpid = "wwf39d4a17555d0bb6"
        # corpsecret = "5timW2hZA_80OcpSUkrl4lSuF3ZiIuJt9qFqQ5-MMkw"

        parm = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        red = {
            "method" : "get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params" : parm
        }
        r = self.send_requests(red)
        self.token = r.json()["access_token"]  #直接定义一个self.token   子类继承时可直接调用
        return self.token  #返回self token