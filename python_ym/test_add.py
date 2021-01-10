import pytest
import yaml

from python_ym.add import add

with open('./yy/dell.yml') as f:
    data = yaml.safe_load(f)["add"]
    do = data["data"]
    myids = data['myids']

with open('./yy/chu.yml') as f:
    chu = yaml.safe_load(f)["chu"]


class Test_add:
    def setup(self):
        self.add = add()
    @pytest.mark.aaa
    @pytest.mark.parametrize(('a,b,c'), [(1, 2, 3), (4, 5, 9), (5, 5, 10)], ids=['aaa', 'bbb', 'ccc'])
    def test_add_1(self, a, b, c):
        aa = self.add.add_1(a, b)
        assert aa == c

    @pytest.mark.parametrize("a,b,c", do, ids=myids)
    def test_dell(self, a, b, c):
        aa = self.add.dell(a, b)
        assert aa == c

    @pytest.mark.parametrize('a,b,c', chu, ids=['1', '2', '3'])
    def test_div(self, a, b, c):
        if isinstance(a,str) or isinstance(b,str):
            raise ValueError('不支持输入字符串')

        try:
            dd=self.add.chu(a,b)
            assert dd ==c
        except:
            print('不支持除数为0')