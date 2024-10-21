import datetime
import time

from model.db.HistoryDate import HistoryDate
from model.db.AnalysisDate import AnalysisDate

from lib.utils import angle, normalize



def press_converter(
    company_code: str,
    date: datetime.date,
    DB = None
) -> list:
    company_code = '4014'
    sdate = date - datetime.timedelta(days=100)
    df = HistoryDate(DB).get_data_by_date_range(
        company_code,
        sdate.strftime('%Y-%m-%d'),
        date.strftime('%Y-%m-%d')
    )

    #print('Data : ', df)
    
    # データが存在しない場合, Noneを返す
    if len(df) <= 29:
        return None

    press_specs = []

    for _r in df:
        open = _r[3]
        high = _r[4]
        low = _r[5]
        close = _r[6]
        r = identify_candle(open, close, high, low)
        print(open, high, low, close, r)
        time.sleep(0.3)
    return 0, 0

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
    

    # 陽場
    if open_price < close_price:
        # 始値と終値が中央値より低い
        if position == 'low':
            if op == 0 and cp >= 2:
                return "強トンカチ陽", 'low', op + cp
            elif op == 0 and cp >= 3:
                return "弱トンカチ陽", 'low', op + cp
            elif op == 0 and cp >= 2:
                return "強トンカチ陽", 'low', op + cp
            elif op == 2 and cp == 2 or op == 1 and cp == 1 or op == 0 and cp == 0:
                return "塔場陽", 'low', op + cp
            return "上影コマ陽線", 'low', op + cp
        
        # 始値と終値が中央値より高い
        elif position == 'high':
            if cp == 8 and op <= 5:
                return "強カラカサ陽", 'high', op + cp
            elif cp == 8 and op <= 6:
                return "弱いカラカサ陽", 'high', op + cp
            elif cp == 6 and op == 6 or cp == 7 and op == 7 or cp == 8 and op == 8:
                return "トンボ陽", 'high', op + cp
            return "下影コマ陽", 'high', op + cp

        # 始値が中央値より低く、終値が中央値より高い
        if cp == 8 and op == 0:
            return "丸坊主陽", 'middle', op + cp
        if cp == 8 and op > 0 and op < 2:
            return "寄付き坊主陽", 'middle', op + cp
        if op == 0 and cp < 8 and cp > 6:
            return "大引け坊主陽", 'middle', op + cp
        elif cp == 7 and op == 1 or cp == 6 and op == 2 or cp == 5 and op == 3:
            return "小陽線", 'middle', op + cp
        elif cp >= 4 and op <= 2:
            return "上影陽線", 'middle', op + cp
        elif cp >= 7 and op <= 4:
            return "下影陽線", 'middle', op + cp
        else:
            return "ヒゲ陽線", 'middle', op + cp
    
    # 陰場
    elif open_price > close_price:
        # 始値と終値が中央値より低い
        if position == 'low':
            if cp == 0 and op >= 2:
                return "強トンカチ陰", 'low', op + cp
            elif cp == 0 and op >= 3:
                return "弱トンカチ", 'low', op + cp
            elif op == 2 and cp == 2 or op == 1 and cp == 1 or op == 0 and cp == 0:
                return "塔場陰", 'low', op + cp
            return "上影コマ陰線", 'low', op + cp
        
        # 始値と終値が中央値より高い
        elif position == 'high':
            if op == 8 and cp <= 5:
                return "強カラカサ陰", 'high', op + cp
            if op == 8 and cp <= 6:
                return "弱カラカサ影", 'high', op + cp
            elif cp == 6 and op == 6 or cp == 7 and op == 7 or cp == 8 and op == 8:
                return "トンボ陰", 'high', op + cp
            return "下影コマ陰線", 'high', op + cp

        # 始値が中央値より低く、終値が中央値より高い
        if op == 8 and cp == 0:
            return "丸坊主陰", 'middle', op + cp
        if op == 8 and cp < 2:
            return "大引け坊主陰", 'middle', op + cp
        if cp == 0 and op > 6:
            return "寄付き坊主陰", 'middle', op + cp
        elif op == 7 and cp == 1 or op == 6 and cp == 2 or op == 5 and cp == 3:
            return "小陰線",  'middle', op + cp
        elif op >= 4 and cp <= 2:
            return "上影陰線", 'middle', op + cp
        elif op >= 7 and cp <= 4:
            return "下影陰線", 'middle', op + cp
        else:
            return "ヒゲ飲泉", 'middle', op + cp
    
    # 始値と終値が同じ
    else:
        if position == 'low':
            if op == 0 or op == 1:
                return "塔場", 'low', op + cp
            elif op == 2 or op == 3:
                return "うわひげ十字", 'low', op + cp
            elif op == 4:
                return "十字", 'low', op + cp
            return "十字", 'low', op + cp
        
        elif position == 'high':
            if op == 8 or op == 7:
                return "トンボ", 'high', op + cp
            elif op == 6 or op == 5:
                return "しもひげ十字", 'high', op + cp
            elif op == 4:
                return "十字", 'high', op + cp
            return "十字", 'high', op + cp
        
        else:
            return "？？", 'middle', op + cp


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

    if open_price < mps[4] and close_price < mps[4]:
        return 'low', check_mps(close_price, mps), check_mps(open_price, mps)
    elif open_price > mps[4] and close_price > mps[4]:
        return 'high', check_mps(close_price, mps), check_mps(open_price, mps)
    else:
        return 'middle', check_mps(close_price, mps), check_mps(open_price, mps)

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