import yaml
from jsonpath import jsonpath

from python_request.api.department import Department


class TestCase:
    def setup_class(self):
        self.department = Department()
        with open('config.yaml') as f:
            config_infor = yaml.safe_load(f)

        self.department.get_token(config_infor["token"]["department_secret"])

    def test_creat_department(self):
        self.department.creat_department(2)
        list = self.department.list_department()
        name = jsonpath(list, "$..name")
        assert "广州研发中心" in name

    def test_update_department(self):
        self.department.updeat_department(2)
        list = self.department.list_department()
        name = jsonpath(list, "$..name")
        print(list)
        assert "小李" in name

    def test_delete_department(self):
        self.department.delete_depatment(2)
        list = self.department.list_department()
        print(list)
        name = jsonpath(list, "$..name")
        assert "小李" not in name
