import requests
import pytest

class Test_tagname:
    def setup_class(self):
        '''定义token'''
        corpid = "wwf39d4a17555d0bb6"
        corpsecret = "5timW2hZA_80OcpSUkrl4lSuF3ZiIuJt9qFqQ5-MMkw"
        access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        parm = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(url=access_token, params=parm)
        self.token = r.json()["access_token"]
    #参数化 断言也可参数化
    @pytest.mark.parametrize("tagname,tagid,errcode",[("汉字",1,0),
                                                     ("",1,40072),
                                                     ("汉字",1,40068),
                                                     ("d字","",0)])
    def test_creat_tagname(self,tagname,tagid,errcode):
        '''创建标签'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {

            "tagname": tagname,
            "tagid": tagid

        }
        r = requests.post(url=url,json=data)
        print(r.json())
        #断言返回的值
        assert r.json()['errcode'] == errcode

