import datetime
import time
import math

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate
from model.schema.CandlePattern import CandlePattern

from lib.utils import angle, normalize, aggregate_stock_data

class PressSpecType:
    candle: dict[
        'key'   : str,
        'name'  : str,
        'code'  : str,
        'trend' : 'sun' or 'shadow' or 'edge',
        'position'  : 'top' or 'middle' or 'low',
        'score' : float
    ]
    price: dict[
        'open'  : float,
        'close' : float,
        'high'  : float,
        'low'   : float
    ]

def press_converter(
    company_code: str,
    date: datetime.date,
    DB = None
) -> tuple:
    #company_code = '4014'
    sdate = date - datetime.timedelta(days=100)
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        sdate.strftime('%Y-%m-%d'),
        date.strftime('%Y-%m-%d')
    )

    #print('Data : ', df)
    
    # データが存在しない場合, Noneを返す
    if len(df) <= 49:
        return None
    df1 = aggregate_stock_data(df, 1)
    df2 = aggregate_stock_data(df, 2)
    df3 = aggregate_stock_data(df, 3)
    df4 = aggregate_stock_data(df, 4)
    df5 = aggregate_stock_data(df, 5)
    
    return candle_converter(df1), candle_converter(df2), candle_converter(df3), candle_converter(df4), candle_converter(df5)

def candle_converter(
    df: list,
) -> list[PressSpecType]:

    press_specs = []
    
    for _r in df:
        open = _r['open']
        high = _r['high']
        low = _r['low']
        close = _r['close']
        if math.isnan(open) or math.isnan(high) or math.isnan(low) or math.isnan(close):
            continue

        r, position, score = identify_candle(open, close, high, low)
        #print(open, high, low, close, r, position, score)

        press_specs.append({
            'candle': {
                'key': r,
                'name': CandlePattern[0][r]['name'],
                'code': CandlePattern[0][r]['code'],
                'trend': CandlePattern[0][r]['trend'],
                'position': position,
                'score': score
            },
            'price': {
                'open': float(open),
                'close': float(close),
                'high': float(high),
                'low': float(low)
            }
        })
    return press_specs
'''
価格情報からローソク足の種類を返す
'''
def identify_candle(
    open_price,
    close_price,
    high_price,
    low_price
) -> tuple:
    position, cp, op = band_position(open_price, close_price, high_price, low_price)
    
    result = []

    # 陽場
    if open_price < close_price:
        # 始値と終値が中央値より低い
        if position == 'low':
            if op == 0 and cp >= 2:
                result = ["strong_hummer_sun", 'low']
            elif op == 0 and cp >= 3:
                result = ["weak_hummer_sun", 'low']
            elif op == 2 and cp == 2 or op == 1 and cp == 1 or op == 0 and cp == 0:
                result = ["tower_top", 'low']
            else:
                result = ["upper_shadow_top_sun", 'low']
        
        # 始値と終値が中央値より高い
        elif position == 'high':
            if cp == 8 and op <= 5:
                result = ["strong_umbrella_sun", 'high']
            elif cp == 8 and op <= 6:
                result = ["weak_umbrella_sun", 'high']
            elif cp == 6 and op == 6 or cp == 7 and op == 7 or cp == 8 and op == 8:
                result = ["dragonfly_sun", 'high']
            else:
                result = ["lower_shadow_top_sun", 'high']

        # 始値が中央値より低く、終値が中央値より高い
        else:
            if cp == 8 and op == 0:
                result = ["bold_head_sun", 'middle']
            if cp == 8 and op > 0 and op < 2:
                result = ["open_bold_head_sun", 'middle']
            if op == 0 and cp < 8 and cp > 6:
                result = ["close_bold_head_sun", 'middle']
            elif cp == 7 and op == 1:
                result = ["large_sun", 'middle']
            elif cp == 6 and op == 2 or cp == 5 and op == 3:
                result = ["small_sun", 'middle']
            elif cp >= 4 and op <= 2:
                result = ["upper_shadow_sun", 'middle']
            elif cp >= 7 and op <= 4:
                result = ["lower_shadow_sun", 'middle']
            else:
                result = ["whisker_sun", 'middle']
            # OPをスコア計算用に補正
            op = 8 - op

    # 陰場
    elif open_price > close_price:
        # 始値と終値が中央値より低い
        if position == 'low':
            if cp == 0 and op >= 2:
                result = ["strong_hummer_shadow", 'low']
            elif cp == 0 and op >= 3:
                result = ["weak_hummer_shadow", 'low']
            elif op == 2 and cp == 2 or op == 1 and cp == 1 or op == 0 and cp == 0:
                result = ["tower_bottom", 'low']
            else:
                result = ["upper_shadow_bottom_shadow", 'low']
            cp = 8 - cp
            op = 8 - op
        
        # 始値と終値が中央値より高い
        elif position == 'high':
            if op == 8 and cp <= 5:
                result = ["strong_umbrella_shadow", 'high']
            if op == 8 and cp <= 6:
                result = ["weak_umbrella_shadow", 'high']
            elif cp == 6 and op == 6 or cp == 7 and op == 7 or cp == 8 and op == 8:
                result = ["dragonfly_shadow", 'high']
            else:
                result = ["lower_shadow_bottom_shadow", 'high']
            cp = 8 - cp

        # 始値が中央値より低く、終値が中央値より高い
        else:
            if op == 8 and cp == 0:
                result = ["bold_head_shadow", 'middle']
            if op == 8 and cp < 2:
                result = ["close_bold_head_shadow", 'middle']
            if cp == 0 and op > 6:
                result = ["open_bold_head_shadow", 'middle']
            elif op == 7 and cp == 1:
                result = ["large_shadow", 'middle']
            elif op == 6 and cp == 2 or op == 5 and cp == 3:
                result = ["small_shadow",  'middle']
            elif op >= 4 and cp <= 2:
                result = ["upper_shadow_shadow", 'middle']
            elif op >= 7 and cp <= 4:
                result = ["lower_shadow_shadow", 'middle']
            else:
                result = ["whisker_shadow", 'middle']
            # OPをスコア計算用に補正
            cp = 8 - cp

    # 始値と終値が同じ
    else:
        # 0~3の場合
        if position == 'low':
            if op == 0 or op == 1:
                result = ["tower", 'low']
            elif op == 2 or op == 3:
                result = ["upper_shadow_cross", 'low']
            elif op == 4:
                result = ["cross", 'low']
            else:
                result = ["cross", 'low']
        # 5~8の場合
        elif position == 'high':
            if op == 8 or op == 7:
                result = ["dragonfly", 'high']
            elif op == 6 or op == 5:
                result = ["lower_shadow_cross", 'high']
            elif op == 4:
                result = ["cross", 'high']
            else:
                result = ["cross", 'high']
        # 4の場合
        else:
            result = ["four_value_same", 'middle']

    result.append(score_result(op, cp))
    return tuple(result)

'''
スコアを正規化する
'''
def score_result(
    op: int,
    cp: int,
) -> int:
    # 16で正規化し、小数点以下2桁で四捨五入
    return round((op + cp) / 16, 2)
    

'''
ローソクが、ローソク足の中でどの位置にあるかを返す
'''
def band_position(
    open_price: float,
    close_price: float,
    high_price: float,
    low_price: float
) -> tuple:
    mps = math_pice_set(high_price, low_price)
    try:
        if open_price < mps[4] and close_price < mps[4]:
            return 'low', check_mps(close_price, mps), check_mps(open_price, mps)
        elif open_price > mps[4] and close_price > mps[4]:
            return 'high', check_mps(close_price, mps), check_mps(open_price, mps)
        else:
            return 'middle', check_mps(close_price, mps), check_mps(open_price, mps)
    except:
        print('Error : ', open_price, close_price, high_price, low_price)
        print('Error : ', mps)

'''
ローソクの幅とローソク足の幅の比率、ローソク足の幅と始値の比率を
変動幅10%を最大、0%を最小に正規化した値と、比率情報を返す
'''
def band_width(
    open_price: float,
    close_price: float,
    high_price: float,
    low_price: float
) -> tuple:
    band_1 = high_price - low_price
    band_2 = open_price - close_price
    # ローソク幅とヒゲ幅の比率
    band_rate_1 = band_2 / band_1
    # ヒゲ幅と始値の比率
    band_rate_2 = band_1 / open_price

    return normalize(band_rate_1, 0, 0.1), normalize(band_rate_2, 0, 0.1), band_rate_1, band_rate_2

'''
値幅を8分割した値を返す
0: 最低値  low_price
1: 最低値 + 1/8
2: 最低値 + 2/8
3: 最低値 + 3/8
4: 最低値 + 4/8 (中央値)
5: 最低値 + 5/8
6: 最低値 + 6/8
7: 最低値 + 7/8
8: 最高値 high_price
'''
def math_pice_set(
    high_price: float,
    low_price: float,
) -> list:
    c1 = high_price - low_price
    c2 = round(c1 / 8, 2)

    return [
        low_price,
        low_price + c2,
        low_price + c2 * 2,
        low_price + c2 * 3,
        low_price + c2 * 4,
        low_price + c2 * 5,
        low_price + c2 * 6,
        low_price + c2 * 7,
        high_price
    ]

'''
値段がmath_price_setのどの範囲にあるかを返す
'''
def check_mps(
    price: float,
    mps: list
) -> int:
    for idx, p in enumerate(mps):
        if price <= p:
            return idx
    return 8