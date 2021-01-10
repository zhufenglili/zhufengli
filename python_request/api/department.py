from python_request.api.wework import WeWork


class Department(WeWork):
    def creat_department(self, tagid):
        '''新增部门'''
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": tagid
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
            "json": data
        }
        r = self.send_request(req)
        return r.json()

    def updeat_department(self, tagid):
        '''更新部门'''
        data = {
            "id": tagid,
            "name": "小李",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        req = {
            "method": "post",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}',
            "json": data
        }
        r = self.send_request(req)
        print(r.json())
        return r.json()

    def delete_depatment(self, tagid):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={tagid}",

        }
        r = self.send_request(req)
        return r.json()
    def list_department(self):
        req={
            "method":"get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        }
        r=self.send_request(req)
        return r.json()