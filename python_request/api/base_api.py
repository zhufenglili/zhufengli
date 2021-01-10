import requests


class Base_api:
    def send_request(self,req:dict):
        return requests.request(**req)