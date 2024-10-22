

def detect_three_soldiers(
    prices1,
    prices2,
    prices3
):
    patterns = []

    day1 = prices1['price']
    day2 = prices2['price']
    day3 = prices3['price']

    score = 0
    
    # 陽の三兵の条件
    if (day1['close'] > day1['open'] and
        day2['close'] > day2['open'] and
        day3['close'] > day3['open'] and
        day2['open'] > day1['open'] and
        day2['close'] > day1['close'] and
        day3['open'] > day2['open'] and
        day3['close'] > day2['close']):
        
        if prices1['candle']['key'] == 'srong_hummer_sun': score -= 3
        if prices2['candle']['key'] == 'srong_hummer_sun': score -= 3
    
    # 陰の三兵の条件
    if (day1['close'] < day1['open'] and
        day2['close'] < day2['open'] and
        day3['close'] < day3['open'] and
        day2['open'] < day1['open'] and
        day2['close'] < day1['close'] and
        day3['open'] < day2['open'] and
        day3['close'] < day2['close']):
        print('陰の三兵')
    
    return patterns

'''
三空のパターンを検出する
'''
def detect_three_gaps(prices):
    patterns = []
    for i in range(len(prices) - 2):
        day1 = prices[i]
        day2 = prices[i + 1]
        day3 = prices[i + 2]
        
        # 上昇三空の条件
        if (day2['Low'] > day1['High'] and
            day3['Low'] > day2['High']):
            patterns.append((i, i + 1, i + 2, '上昇三空'))
        
        # 下降三空の条件
        if (day2['High'] < day1['Low'] and
            day3['High'] < day2['Low']):
            patterns.append((i, i + 1, i + 2, '下降三空'))
    
    return patterns