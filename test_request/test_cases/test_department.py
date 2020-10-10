from test_request.api.department import DeparTment
from test_request.api.wework import WeWork


class Test_department():
    '''用例'''

    def setup_class(self):
        WeWorkk = WeWork()
        self.token = WeWorkk.get_token()
        self.DeparTment = DeparTment()

    def test_creat_department(self):
        self.DeparTment.create_departarment(self.token, 3)
        list = self.DeparTment.list_departarment(self.token)
        assert list["department"][1]["name"] == '宣传部门'

    def test_updeat_department(self):
        self.DeparTment.update_departarment(self.token)
        list = self.DeparTment.list_departarment(self.token)
        assert list["department"][1]["name"] == '广州研发中心'

    def test_delete_departarment(self):
        self.DeparTment.delete_departarment(self.token, 3)
        list = self.DeparTment.list_departarment(self.token)
        assert len(list["department"]) == 1

    def test_list(self):
        self.DeparTment.list_departarment(self.token)
