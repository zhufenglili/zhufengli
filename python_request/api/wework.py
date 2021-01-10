'''token'''

from python_request.api.base_api import Base_api




class WeWork(Base_api):
    def get_token(self,corpsecret):
        corpid = 'wwf39d4a17555d0bb6'
        # corpsecret = '5timW2hZA_80OcpSUkrl4juZWM-31qMER8Yi_WGMr_8'
        # params={"corpid":corpid,"corpsecret":corpsecret}

        req = {
            "url": f' https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}',
            "method": 'get'

        }
        r =self.send_request(req)

        self.token = r.json()['access_token']
        return self.token
