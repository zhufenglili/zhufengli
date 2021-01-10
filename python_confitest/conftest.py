import pytest
@pytest.fixture()
def aaa():
    print('测试开始')
    yield
    print('测试结束')