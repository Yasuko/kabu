import requests
import json

'''
投資部門別情報取得
'''

idToken = "YOUR idToken"
headers = {'Authorization': 'Bearer {}'.format(idToken)}
r = requests.get("https://api.jquants.com/v1/markets/trades_spec?section=TSEPrime&from=20230324&to=20230403", headers=headers)
r.json()