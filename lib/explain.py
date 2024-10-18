import pandas as pd
import datetime
import math
import json

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate

from lib.utils import angle, normalize



def press_converter(
    company_code: str,
    date: datetime.date,
    DB = None
) -> list:
    sdate = date - datetime.timedelta(days=50)
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        sdate.strftime('%Y-%m-%d'),
        date.strftime('%Y-%m-%d')
    )
    
    # データが存在しない場合, Noneを返す
    if len(df) <= 29:
        return None

    press_specs = []

    for idx, _r in df:
        open = _r[3]
        high = _r[4]
        low = _r[5]
        close = _r[6]

        diff_open = close - open
        diff_width = high - low

        # 単純な上昇率 0~1
        up_point = 0
        # 上昇圧 1が最大 0~1
        up_rate = 0
        # 単純な下降率 0~1
        down_point = 0
        # 下降圧 1が最大 0~1
        down_rate = 0
        # 相場の混沌度, 1が最大 -1が最小
        caos_point = 0
        # 上げ下げどちら方向に乱れているか、1が最大-1が最小
        caos_rate = 0

        up_point = round(diff_open / open, 4)
        up_rate =  round((close - open) / (high - low), 4)

        down_point = round(diff_open / close, 4)
        down_rate = round((close - open) / (high - low), 4)

        caos_point = round((high-open+high-close) / (high + low) / (low-open+low-close)/(high+low), 4) + 1

        press_specs.append({
            'up_point': up_point,
            'up_rate': up_rate,
            'down_point': down_point,
            'down_rate': down_rate,
            'caos_point': caos_point,
            'caos_rate': caos_rate
        })
    return 0, 0


def identify_candlestick(open_price, close_price, high_price, low_price):
    if open_price == close_price == high_price == low_price:
        return "四値同事"
    elif open_price == low_price and close_price == high_price:
        return "陽丸坊主"
    elif open_price == high_price and close_price == low_price:
        return "陰丸坊主"
    elif open_price == low_price and high_price > close_price:
        return "陽寄付坊主"
    elif open_price == high_price and low_price < close_price:
        return "陰寄付坊主"
    elif open_price != close_price and high_price == low_price:
        return "大引坊主"
    elif abs(open_price - close_price) < (high_price - low_price) * 0.1:
        return "極線"
    elif open_price == close_price and low_price < open_price and high_price == open_price:
        return "トンボ"
    elif open_price == close_price and high_price > open_price and low_price == open_price:
        return "塔場"
    elif open_price == close_price and high_price > open_price and low_price < open_price:
        return "足長同事"
    elif open_price == close_price and high_price - open_price < open_price - low_price:
        return "たぐり線"
    elif open_price == close_price and low_price < open_price:
        return "カラカサ"
    else:
        return "該当なし"

# テスト
print(identify_candlestick(100, 100, 100, 100))  # 四値同事
print(identify_candlestick(100, 100, 110, 90))   # 寄付坊主
print(identify_candlestick(100, 110, 110, 100))  # 大引坊主
print(identify_candlestick(100, 101, 110, 90))   # 極線
print(identify_candlestick(100, 100, 100, 90))   # トンボ
print(identify_candlestick(100, 100, 110, 100))  # 塔場
print(identify_candlestick(100, 100, 110, 90))   # 足長同事
print(identify_candlestick(100, 100, 105, 90))   # たぐり線
print(identify_candlestick(100, 100, 105, 80))   # カラカサ