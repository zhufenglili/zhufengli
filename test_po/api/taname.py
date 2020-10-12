import requests

from test_po.api.wework import Wework


class Tagname(Wework):
    '''业务'''

    def creat_tagname(self, tagid):
        ''''创建标签'''

        data = {

            "tagname": "第一个标签",
            "tagid": tagid

        }
        red = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": data
        }
        r = self.send_requests(red)
        return r.json()

    def updat_tagname(self, tagid):
        '''更新标签'''
        data = {
            "tagid": tagid,
            "tagname": "更改标签"
        }
        red = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": data
        }

        r = self.send_requests(red)
        return r.json()

    def del_tagname(self, tagid):
        '''删除接口'''

        red = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        }
        r = self.send_requests(red)
        return r.json()

    def list_tagname(self):
        '''列表'''

        red= {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        }
        r_list = self.send_requests(red)
        return r_list.json()
