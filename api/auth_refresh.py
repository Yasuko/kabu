import requests
import json

REFRESH_TOKEN = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Y6c8ujj1djyJTddMgYHAd2E4_8NM50RcIaGipUGYjxdObTyokXDPBA7V2f5TI3Sitj3d2kIlhfZYOR9rU1vyW0YWv8RtEoHWpqQVGR-jlZdhtO3Ji2SDlhUJo4yce2BPU-byOv8adPtYWJSG1w92EDOsdzkIRfuqqdm0biXGUFr-ttxrReGmv8-mDthKFpeVLFOTKpp9SSPlNKK1eXiOfqDjTdEZWC5SZVDZjfbW71XFcrZ6dd2IVBgMu6EfJcyeVGN851HpCScmG1JLzvJ2tzMD3TaELRS1-ScpuP5Y8n2Yhs5N3A8QCE6TjhkyxMH_Q4HG32ok_Qqsl3hPJkfK8g.roxDCAQYbGpxoc6T.2-V8lFgbxpXuWLlhUpYiakkJ28xUboz27FVpEvjlbIe6_6IludqVHwptXH2xwEiNkoZJrzxIcv-DyCpgAbhcGISegy7XOJEbtBLORBnSuANS--WlC7vO-C0ntxvx4Gbf38XYgm8kochdYR3D0pgjOr-iKkRxK-qVz4eDIQrV91rzwbz70rKrY2GA0xouAoSDmnNbIMfoh-NXUItV8geHlBisjufwiV3PUQlQWgivqdiRZQzFIyFoBbmzmCi0CQgA8MwU7CzIU4Ev2ezwhpULFd2ov1W_EaiMb5ZfkSeB20I8KJLj6aMO9oBujqdGsR_Bg9bVky2AJJvjoJHISULGTuk2NtwV_jH3Px4Ji3C2BEnRcP6Upj2N24Fmz6B9tOqf08LGBryLZ9xfpbsyA0yAQlHp0aC217vF5RsLmqr0yZw_jtcOOmstNZspRUZCosC5wX2u8i8a1qZUJI__oThNzjYAY9KYS2nWsqXkk6ov7P34KG9tUB-07u26hANQCUg1W93ZmZk05gb9NiMCvu8lyWXaZx6z6mCG7PbF4fcukOIDMfF1L7fO1sQg7_vPdYCMUA9DeJaBCTyv8PdDO3UjXwDWq8VKj1M_hJamHu8mo2bDYvbeS4HomNGdkCqR118WCCamTYfo-_HsVlxkuYQQl4-dZWZJmMfR6JaQxwEc0VLzx966eX1tjeEdBsnHaaV8G-p3ilGKTT23KVo03glUbXw7oBOEh21qljxKTut5sX5nLyUL0peYb2JTiLIVy12KCdMr_GDDRVVZ89V06jc4Y3mMKGtqz-tK4KjiGQHrJEZglCLnp95DvLu9u565Gibjc1VKjF6BGEbUpJyDAqaPofRzrg4HiWOK2JtlaGiT9icpqsmO_B-McFqZnaFLWCJYN8fdjiZRksnttbYoYyHfGfCh_gz-MwMldaQlEwjvR8GVCslmnB1dJAhyP3kDN_Wp5LuEdQQTs-YLwrqCyIDiZztJGkD2JCo1f3un2WRE9ZhnJXq13_rPbLAyXy9Vic72p3F4Hw7vTQ-CeL1CQZmsPgecl-jj_KNJiV1ZYNJJwt9q5PZpkRvfV0SRh_vO8L1iJskNpzp-unl4oYR0ntF0woKnHH0uQ3GnIe9oz25dNuSnx_DSl9aH6zgS74xcYxlupLQcMilHU3XdG4zLNEePPTV0wgvxQFHcXZxY-UPt8pM7jY--8_E0PVeMfpObq5XtZGZZuWlW01uHuR5fD_OiW2J-fmRLpj1VQ5gB3Xy6jloDh2KmfTxrlnfcr5gs2X5YKUN-dJ4nrbzqFKMliJcwnR__6KPjby9sRi_o8awp-gieYpHH9arNeEl8Mk-FDSZ-hTW3QWLTq_dTHg.VtaieGvzaAWmR2D2ro8k0g"
r_post = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}")
print(r_post.json())

class AuthRefresh:

    _idToken = ""

    def __init__(self, REFRESH_TOKEN):
        self.REFRESH_TOKEN = REFRESH_TOKEN
    
    @property
    def idToken(self):
        return self._idToken

    def call():
        r_post = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={self.REFRESH_TOKEN}")
        if r_post.status_code == 200:
            self._idToken = r_post.json()["idToken"]
            return self._idToken
        else:



