from test_po.api.taname import Tagname
from test_po.api.wework import Wework


class Test_tagname():
    def setup_class(self):
        # 实例化token
        wework = Wework()
        self.token = wework.get_token()
        # 实例化Tagname
        self.tagname = Tagname()

    def test_creat_tagname(self):
        '''创建标签'''
        self.tagname.creat_tagname(self.token, 1)
        list = self.tagname.list_tagname(self.token)  # 标签列表
        assert list["taglist"][0]["tagname"] == '第一个标签'

    def updet_tagname(self):
        '''更新标签'''
        self.tagname.updat_tagname(self.token, 1)
        list = self.tagname.list_tagname(self.token)  # 标签列表
        assert list["taglist"][0]["tagname"] == '更改标签'

    def del_tagname(self):
        '''删除标签'''
        self.tagname.del_tagname(self.token, 1)
        list = self.tagname.list_tagname(self.token)  # 标签列表
        assert list['taglist'] == 1
