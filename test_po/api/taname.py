import requests
class Tagname:
    '''业务'''
    def creat_tagname(self,token,tagid):
        ''''创建标签'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {

            "tagname": "第一个标签",
            "tagid": tagid

        }
        r = requests.post(url=url, json=data)
        return r.json()
    def updat_tagname(self,token,tagid):
        '''更新标签'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        data = {
            "tagid": tagid,
            "tagname": "更改标签"
        }
        r = requests.post(url=url, json=data)
        return r.json()
    def del_tagname(self,token,tagid):
        '''删除接口'''

        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tagid}"
        r = requests.get(url=url)
        return r.json()
    def list_tagname(self,token):
        '''列表'''
        list = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        r_list = requests.get(url=list)
        return r_list.json()