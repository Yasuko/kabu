import requests
import json

"""
リフレッシュトークンを取得
"""

data={"mailaddress":"ton_ma@hotmail.com", "password":"qcF6wk3wd84TYtX"}
r_post = requests.post("https://api.jquants.com/v1/token/auth_user", data=json.dumps(data))
print(r_post.json())