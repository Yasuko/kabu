import lib.callapi as callapi

"""
投資部門別情報

"""

END_POINT = "https://api.jquants.com/v1/markets/trades_spec"

class OptionsType:
    section: str = ""
    from_date: str = ""
    to_date: str = ""
    pagenation_key: str = ""

class TradeSpecCall:

    def call(self, Options: OptionsType, idToken):
        if Options.pagenation_key == "":
            url = f"{END_POINT}?section={Options.section}&from={Options.from_date}&to={Options.to_date}"
        else:
            url = f"{END_POINT}?section={Options.section}&from={Options._from_date}&to={Options._to_date}&pagenation_key={Options._pagenation_key}"

        result = callapi.CallAPI(idToken).get(url)
        if result.status_code == 200:
            data = result.json()
            if 'pagenation_key' in data:
               self._pagenation_key = data['pagenation_key']
            else:
                self._pagenation_key = ""
            return data['trades_spec']
        else:
            print(f"Error: {result['message']}")
            return None



