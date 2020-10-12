import requests
from jsonpath import jsonpath


class Baseapi:
    def send_requests(self,red:dict):
        ''''封装requests'''

        return requests.request(**red)

    def get_jsonpath(self,objj,bao):
        return jsonpath(objj,bao)