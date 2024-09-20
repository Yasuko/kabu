import requests
import json

'''
財務諸表取得
'''

idToken = "YOUR idToken"
headers = {'Authorization': 'Bearer {}'.format(idToken)}
r = requests.get("https://api.jquants.com/v1/fins/fs_details?code=86970&date=20230130", headers=headers)
r.json()