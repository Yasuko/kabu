import requests
import json

class CallAPI:
    def __init__(self, idToken):
        self.setToken(idToken)

    def setToken(self, idToken):
        self.idToken = idToken
        self.headers = {
                'Authorization':
                    'Bearer {}'.format(self.idToken)
            }

    def get(self, url, headers: bool = True):
        if headers:
            r = requests.get(url, headers=self.headers)
        else:
            r = requests.get(url)
        return r.json()
    
    def post(self, url, data, headers: bool = True):
        if headers:
            r = requests.post(url, headers=self.headers, data=data)
        else:
            r = requests.post(url, data=data)
        return r.json()
    
    def put(self, url, data, headers: bool = True):
        if headers:
            r = requests.put(url, headers=self.headers, data=data)
        else:
            r = requests.put(url, data=data)
        return r.json()
    
    def delete(self, url, headers: bool = True):
        if headers:
            r = requests.delete(url, headers=self.headers)
        else:
            r = requests.delete(url)
        return r.json()
    


