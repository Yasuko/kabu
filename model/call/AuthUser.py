import lib.callapi as callapi
import json

"""
 リフレッシュトークン取得 auth_user

 ※ リフレッシュトークンの有効期限は１週間
"""

END_POINT = "https://api.jquants.com/v1/token/auth_user"

class OptionsType:
    mailaddress: str = ""
    password: str = ""

class AuthUser:

    def call(self, Options: OptionsType):
        result = callapi.CallAPI('').post(END_POINT, data=json.dumps(Options))
        if "refreshToken" in result:
            return result['refreshToken']
        else:
            print(f"Error: {result['message']}")
            return None



"""
■ Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/refreshtoken


■ Return Value
変数名	        説明	            型	        備考
refreshToken    リフレッシュトークン String

■ Example

import requests
import json

data={"mailaddress":"<YOUR EMAIL_ADDRESS>", "password":"<YOUR PASSWORD>"}
r_post = requests.post("https://api.jquants.com/v1/token/auth_user", data=json.dumps(data))
r_post.json()

"""