import requests
class TestReqest:
    '''
    获取token
    '''
    def test_reqest(self):
        corpid = "wwf39d4a17555d0bb6"
        corpsecret ="5timW2hZA_80OcpSUkrl4vgTL5JVusjH9gxJgJCP2Xk"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.json())
    def test_requests(self):
        "获取token"
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4vgTL5JVusjH9gxJgJCP2Xk"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params ={
            "corpid" : corpid,
            "corpsecret" : corpsecret
        }
        r = requests.get(url=url,params=params)
        print(r.json())