import lib.callapi as callapi
import json

"""
 IDトークン取得 auth_refresh

 ※ リフレッシュトークンの有効期限は１週間
 ※ IDトークンの有効期限は24時間
"""

END_POINT = "https://api.jquants.com/v1/token/auth_refresh"

class OptionsType:
    refreshtoken: str = ""

class AuthRefresh:
   
    def call(self, Options: OptionsType):
        url = f"{END_POINT}?refreshtoken={Options['refreshtoken']}"
        result = callapi.CallAPI('').post(url, {})
        if "idToken" in result:
            return result['idToken']
        else:
            print(f"Error: {result['message']}")
            return None



"""
■ Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/idtoken


■ Return Value
変数名	        説明	            型	        備考
idToken        IDトークン           String

■ Example

import requests
import json

REFRESH_TOKEN = "YOUR refreshtokenID"
r_post = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}")
r_post.json()

"""