import requests
def test_dome():
    url = 'http://httpbin.testing-studio.com/cookies'
    header={
        'huogeg':'lsdkf',
    }
    cookie_d ={
        "sdflksdf":"lililili",
        "lskdjksdfj":"ooooooo"
               }
    r =requests.get(url=url,headers = header,cookies=cookie_d)
    print(r.request.headers)