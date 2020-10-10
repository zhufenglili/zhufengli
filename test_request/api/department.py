import requests


class DeparTment:
    '''业务层'''

    def create_departarment(self,token,department_id):
        '''添加部门'''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        param = {

            "access_token": token

        }
        data = {
            "name": "宣传部门",
            "name_en": "jdk",
            "parentid": 1,
            "order": 9,
            "id": department_id
        }

        r = requests.post(url=url, json=data, params=param)
        return r.json()

    def update_departarment(self,token):
        '''更新部门'''
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        data = {
            "id": 3,
            "name": "广州研发中心",
            "name_en": "jdk",
            "parentid": 1,
            "order": 9
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_departarment(self,token,department_id):
        '''删除部门'''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=url)
        return r.json()

    def list_departarment(self,token):
        '''部门列表'''
        list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
        list = requests.get(url=list_url)
        return list.json()
