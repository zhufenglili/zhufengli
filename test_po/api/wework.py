import requests
class Wework():
    '''token'''
    def get_token(self):
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
        return r.json()["access_token"]