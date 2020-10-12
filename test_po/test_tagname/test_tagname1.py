import yaml
from jsonpath import jsonpath

from test_po.api.taname import Tagname
from test_po.api.wework import Wework


class Test_tagname():
    def setup_class(self):
        # 实例化Tagname
        self.tagname = Tagname()
        secret_s = yaml.safe_load(open('secret.yaml'))
        self.tagname.get_token(secret_s["token"]["d_secret"])

    def test_creat_tagname(self):
        '''创建标签'''
        self.tagname.creat_tagname(1)
        list = self.tagname.list_tagname()
        print(list)  # 打印列表
        name = self.tagname.get_jsonpath(list, "$..tagname")
        assert '第一个标签' in name  # 断言添加的标签在jsonpath中

    def test_update_tagname(self):
        '''更新标签'''
        self.tagname.updat_tagname(1)
        list = self.tagname.list_tagname()  # 标签列表
        print(list)
        name = self.tagname.get_jsonpath(list, "$..tagname")
        assert "更改标签" in name

    def test_del_tagname(self):
        '''删除标签'''
        self.tagname.del_tagname(1)
        list = self.tagname.list_tagname()  # 标签列表
        print(list)
        id_1 = self.tagname.get_jsonpath(list,"$..taglist")
        assert 1 not in id_1


