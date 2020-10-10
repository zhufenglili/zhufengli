import requests
from jsonpath import  jsonpath

class Test_request:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/#/HTTP_Methods/get_get")
        print(r.status_code)
        print(r.text)
        # print(r.json())
        assert r.status_code == 200

    def test_heads(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={"H":"lallsdkf"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.json()["headers"]["H"]=='lallsdkf'
    def test_json(self):
        palyload ={
            "name":"li",
            "age" : 12

        }
        r = requests.post("http://httpbin.testing-studio.com/post",json=palyload)
        print(r.text)
        print(r.json())
        assert r.json()["json"]["age"] == 12