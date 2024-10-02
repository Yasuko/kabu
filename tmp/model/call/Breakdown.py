import lib.callapi as callapi

"""
 売買内訳データ breakdown
"""

END_POINT = "https://api.jquants.com/v1/markets/breakdown"

class OptionsType:
    code: str = ""
    date: str = ""
    from_date: str = ""
    to_date: str = ""
    pagenation_key: str = ""

class BreakdownCall:
   
    def call(self, Options: OptionsType, idToken):
        if Options.date == "":
            url = f"{END_POINT}?code={Options.code}&from={Options.from_date}&to={Options.to_date}"
        else :
            if Options.pagenation_key == "":
                url = f"{END_POINT}?code={Options.code}&date={Options.date}"
            else:
                url = f"{END_POINT}?code={Options.code}&date={Options.date}&pagenation_key={Options.pagenation_key}"

        result = callapi.CallAPI(idToken).get(url)
        if result.status_code == 200:
            data = result.json()
            if 'pagenation_key' in data:
               self._pagenation_key = data['pagenation_key']
            else:
                self._pagenation_key = ""
            return data['breakdown']
        else:
            print(f"Error: {result['message']}")
            return None







"""
Sample Doc

https://jpx.gitbook.io/j-quants-ja/api-reference/breakdown

Date 売買日 String YYYY-MM-DD
Code 銘柄コード String
LongSellValue 実売りの約定代金 Number 売りの約定代金の内訳
ShortSellWithoutMarginValue 空売り(信用新規売りを除く)の約定代金 Number 同上
MarginSellNewValue 信用新規売り(新たな信用売りポジションを作るための売り注文)の約定代金 Number 同上
MarginSellCloseValue  信用返済売り(既存の信用買いポジションを閉じるための売り注文)の約定代金 Number 同上
LongBuyValue 現物買いの約定代金 Number 買いの約定代金の内訳
MarginBuyNewValue 信用新規買い(新たな信用買いポジションを作るための買い注文)の約定代金 Number 同上
MarginBuyCloseValue 信用返済買い(既存の信用売りポジションを閉じるための買い注文)の約定代金 Number 同上
LongSellVolume 実売りの約定株数 Number 売りの約定株数の内訳
ShortSellWithoutMarginVolume 空売り(信用新規売りを除く)の約定株数 Number 同上
MarginSellNewVolume 信用新規売り(新たな信用売りポジションを作るための売り注文)の約定株数 Number 同上
MarginSellCloseVolume 信用返済売り(既存の信用買いポジションを閉じるための売り注文)の約定株数 Number 同上
LongBuyVolume 現物買いの約定株数 Number 買いの約定株数の内訳
MarginBuyNewVolume 信用新規買い(新たな信用買いポジションを作るための買い注文)の約定株数 Number 同上
MarginBuyCloseVolume  信用返済買い(既存の信用売りポジションを閉じるための買い注文)の約定株数 Number 上　


"""