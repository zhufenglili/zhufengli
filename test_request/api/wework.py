import requests
class WeWork:
    def get_token(self):
        '''获取token'''
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4lSuF3ZiIuJt9qFqQ5-MMkw"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"


        params = {
            "corpid": corpid,
            "corpsecret": corpsecret

        }

        r = requests.get(url=url, params=params)
        #返回token数据
        return r.json()["access_token"]
