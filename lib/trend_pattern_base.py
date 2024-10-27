'''
陽の包み線を検出する

陰線をつけた翌日に、陽線をつけて尚且つ
1日目の始値よりも、2日目の始値が低く
1日目の終値よりも、2日目の終値が高い場合

シグナル
    下降トレンド時は、上昇トレンドに転換

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陽の包み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bullish_engulfing(
    prev_candle,
    candle
) -> bool:
    # 陰線をつけた翌日に、陽線をつけて尚且つ
    if (prev_candle['close'] < prev_candle['open'] and candle['close'] > candle['open']
        # 1日目の始値よりも、2日目の始値が低く(1%以上)
        and candle['open'] < (prev_candle['close'] - (prev_candle['close'] * 0.01))
        # 1日目の終値よりも、2日目の終値が高い(1%以上)
        and candle['close'] > (prev_candle['open'] + (prev_candle['open'] * 0.01))):
        return True
    
    return False

'''
陰の包み線を検出する

陽線をつけた翌日に、陰線をつけて尚且つ
1日目の始値よりも、2日目の終値が低く
1日目の終値よりも、2日目の始値が高い場合

シグナル
    上昇トレンド時は、下落トレンドに転換

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陰の包み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_engulfing(
    prev_candle,
    candle
) -> bool:
    # 陽線をつけた翌日に、陰線をつけて尚且つ
    if (prev_candle['close'] > prev_candle['open'] and candle['close'] < candle['open']
        # 1日目の始値よりも、2日目の終値が低く(1%以上)
        and candle['open'] > (prev_candle['close'] + (prev_candle['close'] * 0.01))
        # 1日目の終値よりも、2日目の始値が高い(1%以上)
        and candle['close'] < (prev_candle['open'] - (prev_candle['open'] * 0.01))):
        return True
    
    return False

'''
陽のはらみ線を検出する

陽線を付けた翌日に、陽線か陰線を付けて尚且つ
2日目のローソクの足が、1日目のローソクの足の始値と終値の間にある場合

シグナル
    移動平均から
    高値の場合は下降トレンドに転換

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陽のはらみ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bullish_harami(
    prev_candle,
    candle
) -> bool:
    # 1日目が陽線、2日目が陽線
    if (prev_candle['close'] > prev_candle['open']
        and candle['close'] > candle['open']
        # 2日目のローソクの足が、1日目のローソクの始値と終値の間にある(1%以上の差)
        and candle['open'] >= (prev_candle['open'] + (prev_candle['open'] * 0.03))
        and candle['close'] <= (prev_candle['close'] - (prev_candle['close'] * 0.03))):
        return True
    
    # 1日目が陽線、2日目が陰線
    if (prev_candle['close'] > prev_candle['open']
        and candle['close'] < candle['open']
        # 2日目のローソクの足が、1日目のローソクの始値と終値の間にある
        and candle['open'] <= (prev_candle['close'] - (prev_candle['close'] * 0.03))
        and candle['close'] >= (prev_candle['open'] + (prev_candle['open'] * 0.03))):
        return True
    return False

'''
陰のはらみ線を検出する

前日が陰線で、当日が陰線か陽線で尚且つ
前日のローソクの足が、当日のローソクの足より長く
当日のローソクの足が、前日のローソクの足の始値と終値の間にある場合

シグナル
    移動平均から
    安値の場合は上昇トレンドに転換

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 陰のはらみ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_harami(
    prev_candle,
    candle
) -> bool:
    # 1日目が陰線、2日目が陰線
    if (prev_candle['close'] < prev_candle['open']
        and candle['close'] < candle['open']
        # 2日目のローソクの足が、1日目のローソクの足の始値と終値の間にある
        and candle['open'] <= (prev_candle['open'] - (prev_candle['open'] * 0.03))
        and candle['close'] >= (prev_candle['close'] + (prev_candle['close'] * 0.03))):
        return True
    
    # 1日目が陰線、2日目が陽線
    if (prev_candle['close'] < prev_candle['open']
        and candle['close'] > candle['open']
        # 2日目のローソクの足が、1日目のローソクの足の始値と終値の間にある
        and candle['open'] >= (prev_candle['close'] + (prev_candle['close'] * 0.03))
        and candle['close'] <= (prev_candle['open'] - (prev_candle['open'] * 0.03))):
        return True
    
    return False

'''
かぶせ線を検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の始値が1日目の終値よりも高く
2日目の終値が1日目の始値と終値の間にある場合

シグナル
    売り圧強い

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: かぶせ線パターンが検出された場合はTrue、それ以外はFalse
'''
def is_dark_cloud_cover(
    prev_candle,
    curr_candle
):
    # 1日目が大陽線、2日目が大陰線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']):
            # 2日目の始値が1日目の終値よりも高く(1%以上)
            if (curr_candle['open'] > (prev_candle['close'] + (prev_candle['close'] * 0.01))
                # 2日目の終値が1日目の始値と終値の間にある
                and curr_candle['close'] > prev_candle['open']
                and curr_candle['close'] < prev_candle['close']):
                    return True
    return False

'''
切り込み線を検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の終値が1日目の始値と終値の中間値を超えている場合

シグナル
    転換、上昇

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 切り込み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_piercing_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の安値よりも低く
        if (curr_candle['open'] < prev_candle['low']
            # 2日目の終値が1日目の始値と終値の中間値を超えている
            and curr_candle['close'] > (prev_candle['open'] + prev_candle['close']) / 2
            # 2日目の終値が1日目の始値よりも低い
            and curr_candle['close'] < prev_candle['open']):
            return True
    
    return False

'''
差し込み線を検出する

大陰線を付けた翌日に、陽線を付けて尚且つ
2日目のヒゲの部分だけが、1日目の始値と終値の中間値を超えている場合

トレンド
    下げトレンド時は維持
    上げトレンド時は転換

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 差し込み線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_harami_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の安値よりも低い
        if (curr_candle['open'] < prev_candle['low']
            # 2日目の終値が1日目の終値よりも高い
            and curr_candle['close'] > prev_candle['close']
            
            # 2日目の最高値が1日目の始値と終値の中心値を超えている
            and curr_candle['high'] > (prev_candle['close'] + prev_candle['open']) / 2
            # 2日目の終値は1日目の始値と終値の中心値より低い
            and curr_candle['close'] < (prev_candle['close'] + prev_candle['open']) / 2):

            return True
    
    return False

'''
入り首線を検出する

大陰線を付けた翌日に、陽線を付けて尚且つ
2日目の開始値が、前日の終値、最低値よりも低く
2日目の最高値が、1日目の終値より高く、始値と終値の中心値まで届かなかった場合

シグナル
    買い弱

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 入り首線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_in_neck_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値、最低値よりも低い
        if (curr_candle['open'] < prev_candle['close']
            and curr_candle['open'] < prev_candle['low']
            # 2日目の最高値が1日目の終値より高く、始値と終値の中心値まで届かなかった
            and curr_candle['high'] > prev_candle['close']
            and curr_candle['high'] < prev_candle['open'] + prev_candle['close']) / 2:
            return True
    
    return False

'''
あて首線を検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の高値と1日目の終値が離れて、隙間がある場合

シグナル
    売り圧強

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: あて首線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_on_neck_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の高値が1日目の安値よりも1段低い（1%以上）
        if ((prev_candle['low'] > curr_candle['high'] + (curr_candle['high'] * 0.01))):
            return True
    
    return False

'''
出会い線の陽線パターンを検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の終値が1日目の終値とほぼ同じ場合

シグナル
    売り

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 出会い線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_meeting_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陽線、2日目が大陰線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']):

        # 2日目の終値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['close'] < (prev_candle['close'] + (prev_candle['close'] * 0.01))
            and curr_candle['close'] > (prev_candle['close'] - (prev_candle['close'] * 0.01))):
            return True
    
    return False

'''
出会い線の陰線パターンを検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の始値が1日目の終値とほぼ同じ場合

シグナル
    買い

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 出会い線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_meeting_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が大陽線
    if (prev_candle['open'] > prev_candle['close']
        and curr_candle['open'] < curr_candle['close']):

        # 2日目の始値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['open'] > (prev_candle['close'] - (prev_candle['close'] * 0.01))
            and curr_candle['open'] < (prev_candle['close'] + (prev_candle['close'] * 0.01))):
            return True
    
    return False

'''
振り分け線の陽線パターンを検出する

大陰線を付けた翌日に、大陽線を付けて尚且つ
2日目の始値が1日目の始値とほぼ同じ場合

シグナル
    買い

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 振り分け線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_separating_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陰線、2日目が大陽線
    if (prev_candle['open'] > prev_candle['close']
        and curr_candle['open'] < curr_candle['close']):

        # 2日目の始値が1日目の終値とほぼ同じ（1%以内）
        if (curr_candle['open'] <= (prev_candle['open'] + (prev_candle['open'] * 0.01))
            and curr_candle['open'] >= (prev_candle['open'] - (prev_candle['open'] * 0.01))):
            return True
    
    return False

'''
振り分け線の陰線パターンを検出する

大陽線を付けた翌日に、大陰線を付けて尚且つ
2日目の始値が1日目の始値とほぼ同じ場合

シグナル
    売り

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 振り分け線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_separating_lines_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が大陽線、2日目が大陰線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']):

        # 2日目の始値が1日目の始値とほぼ同じ(1%以内)
        if (curr_candle['open'] >= (prev_candle['open'] - (prev_candle['open'] * 0.01))
            and curr_candle['open'] <= (prev_candle['open'] + (prev_candle['open'] * 0.01))):
            return True
    
    return False


'''
タスキ線の陽線パターンを検出する

陰線をつけた翌日に、陽線をつけて尚且つ
2日目の始値が1日目の安値よりも高く、1日目の始値よりも低い
2日目の終値が1日目の高値よりも高い場合(5%以上)

シグナル
    売り

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: タスキ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tasukigap_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陽線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] < curr_candle['close']:
        # 2日目の始値が1日目の終値よりも高く、1日目の始値よりも低い
        if (curr_candle['open'] > prev_candle['close'] # low以上なので、マージンも含めてcloseで指定
            and curr_candle['open'] < prev_candle['open']
            # 2日目の終値が1日目の高値よりも高い(5%以上)
             and curr_candle['close'] > prev_candle['high'] + (prev_candle['high'] * 0.05)):
            return True
    
    return False

'''
タスキ線の陰線パターンを検出する

陽線をつけた翌日に、陰線をつけて尚且つ
2日目の始値が1日目の安値よりも高く、1日目の終値よりも低い
2日目の終値が1日目の安値よりも低い場合(5%以上)

シグナル
    買い

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: タスキ線パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_bearish_tasukigap_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目も陰線
    if prev_candle['open'] > prev_candle['close'] and curr_candle['open'] > curr_candle['close']:
        # 2日目の始値が1日目の安値よりも高く、1日目の終値よりも低い
        if (curr_candle['open'] > prev_candle['low']
            and curr_candle['open'] < prev_candle['close']
            # 2日目の終値が1日目の安値よりも低い(5%以上)
            and curr_candle['close'] < prev_candle['low'] - (prev_candle['low'] * 0.05)):
            return True
    
    return False

'''
毛抜き天井のパターンを検出する

2営業日の高値がほぼ同じ、陰線・陽線は問わない

シグナル
    天井

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き天井パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tweezer_top_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陽線、2日目が陰線・陽線
    if (prev_candle['open'] < prev_candle['close']
        and curr_candle['open'] > curr_candle['close']
        or curr_candle['open'] < curr_candle['close']):
        # 1日目と2日目の高値がほぼ同じ(1%以内)
        if (prev_candle['high'] == curr_candle['high']
            or prev_candle['high'] == (curr_candle['high'] + (curr_candle['high'] * 0.01))
            or prev_candle['high'] == (curr_candle['high'] - (curr_candle['high'] * 0.01))):
            return True
    
    return False

'''
毛抜き底のパターンを検出する

2営業日の安値がほぼ同じ、陰線・陽線は問わない

シグナル
    底

パラメータ:
    prices1 (dict): 1日前の株価情報
    prices2 (dict): 当日の株価情報
戻り値:
    bool: 毛抜き底パターンが検出された場合はTrue、それ以外はFalse
'''
def detect_tweezer_bottom_pattern(
    prev_candle,
    curr_candle
) -> bool:
    # 1日目が陰線、2日目が陰線・陽線
    if (prev_candle['open'] > prev_candle['close']
        and curr_candle['open'] < curr_candle['close']
        or curr_candle['open'] > curr_candle['close']):
        # 1日目と2日目の安値がほぼ同じ(1%以内)
        if (prev_candle['low'] == curr_candle['low']
            or prev_candle['low'] == (curr_candle['low'] + (curr_candle['low'] * 0.01))
            or prev_candle['low'] == (curr_candle['low'] - (curr_candle['low'] * 0.01))):
            return True
    
    return False