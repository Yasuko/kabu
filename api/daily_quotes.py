import requests
import json

'''
株価4本値取得
'''

idToken = "YOUR idToken"
headers = {'Authorization': 'Bearer {}'.format(idToken)}
r = requests.get("https://api.jquants.com/v1/prices/daily_quotes?code=86970&date=20230324", headers=headers)
r.json()