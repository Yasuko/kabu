import lib.callapi as callapi

"""
上場銘柄一覧

"""

END_POINT = "https://api.jquants.com/v1/listed/info"

class OptionsType:
    code: str = ""
    date: str = ""

class Info:

    def call(self, Options: OptionsType, idToken):
        print(Options)
        if Options["code"] != "":
            if Options["date"] != "":
                url = f"{END_POINT}?code={Options['code']}&date={Options['date']}"
            else:
                url = f"{END_POINT}?code={Options['code']}"
        else:
            url = f"{END_POINT}"
        result = callapi.CallAPI(idToken).get(url)
        print(result)
        if "info" in result:
            return result['info']
        else:
            print(f"Error: {result['message']}")
            return None



"""
import requests
import json

idToken = "YOUR idToken"
headers = {'Authorization': 'Bearer {}'.format(idToken)}
r = requests.get("https://api.jquants.com/v1/listed/info", headers=headers)
r.json()
"""