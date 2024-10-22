'''
ローソクパターンのスキーマ定義？
'''

class CandlePatternType:
    name: str
    code: str
    score: int
    open: float
    close: float
    high: float
    low: float

CandlePattern = [
    {
        'strong_hummer_sun' : {
            'name'    : "強トンカチ",
            'code'    : 'strong_hummer',
            'trend'   : 'sun'
        },
        'weak_hummer_sun' : {
            'name'  : "弱トンカチ陽",
            'code'  : 'weak_hummer',
            'trend' : 'sun'
        },
        'tower_top' : {
            'name'  : "塔場陽",
            'code'  : 'tower_top',
            'trend' : 'sun'
        },
        'upper_shadow_top_sun' : {
            'name'  : "上影コマ陽線",
            'code'  : 'upper_top_sun',
            'trend' : 'sun'
        },
        'strong_umbrella_sun' : {
            'name'  : "強カラカサ陽",
            'code'  : 'strong_umbrella',
            'trend' : 'sun'
        },
        'weak_umbrella_sun' : {
            'name'  : "弱いカラカサ陽",
            'code'  : 'weak_umbrella',
            'trend' : 'sun'
        },
        'dragonfly_sun' : {
            'name'  : "トンボ陽",
            'code'  : 'dragonfly',
            'trend' : 'sun'
        },
        'lower_shadow_top_sun' : {
            'name'  : "下影コマ陽",
            'code'  : 'lower_shadow_top',
            'trend' : 'sun'
        },
        'bold_head_sun' : {
            'name'  : "丸坊主陽",
            'code'  : 'bold_head',
            'trend' : 'sun'
        },
        'open_bold_head_sun' : {
            'name'  : "寄付き坊主陽",
            'code'  : 'open_bold_head',
            'trend' : 'sun'
        },
        'close_bold_head_sun' : {
            'name'  : "大引け坊主陽",
            'code'  : 'close_bold_head',
            'trend' : 'sun'
        },
        'large_sun' : {
            'name'  : "大陽線",
            'code'  : 'large',
            'trend' : 'sun'
        },
        'small_sun' : {
            'name'  : "小陽線",
            'code'  : 'small',
            'trend' : 'sun'
        },
        'upper_shadow_sun' : {
            'name'  : "上影陽線",
            'code'  : 'upper_shadow',
            'trend' : 'sun'
        },
        'lower_shadow_sun' : {
            'name'  : "下影陽線",
            'code'  : 'lower_shadow',
            'trend' : 'sun'
        },
        'whisker_sun' : {
            'name'  : "ヒゲ陽線",
            'code'  : 'whisker',
            'trend' : 'sun'
        },
        'strong_hummer_shadow' : {
            'name'  : "強トンカチ陰",
            'code'  : 'strong_hummer',
            'trend' : 'shadow'
        },
        'weak_hummer_shadow' : {
            'name'  : "弱トンカチ",
            'code'  : 'weak_hummer',
            'trend' : 'shadow'
        },
        'tower_bottom' : {
            'name'  : "塔場陰",
            'code'  : 'tower_bottom',
            'trend' : 'shadow'
        },
        'upper_shadow_bottom_shadow' : {
            'name'  : "上影コマ陰線",
            'code'  : 'upper_shadow_bottom',
            'trend' : 'shadow'
        },
        'strong_umbrella_shadow' : {
            'name'  : "強カラカサ陰",
            'code'  : 'strong_umbrella',
            'trend' : 'shadow'
        },
        'weak_umbrella_shadow' : {
            'name'  : "弱カラカサ陰",
            'code'  : 'weak_umbrella',
            'trend' : 'shadow'
        },
        'dragonfly_shadow' : {
            'name'  : "トンボ陰",
            'code'  : 'dragonfly',
            'trend' : 'shadow'
        },
        'lower_shadow_bottom_shadow' : {
            'name'  : "下影コマ陰線",
            'code'  : 'lower_bottom',
            'trend' : 'shadow'
        },
        'bold_head_shadow' : {
            'name'  : "丸坊主陰",
            'code'  : 'bold_head',
            'trend' : 'shadow'
        },
        'close_bold_head_shadow' : {
            'name'  : "大引け坊主陰",
            'code'  : 'close_bold_head',
            'trend' : 'shadow'
        },
        'open_bold_head_shadow' : {
            'name'  : "寄付き坊主陰",
            'code'  : 'open_bold_head',
            'trend' : 'shadow'
        },
        'large_shadow' : {
            'name'  : "大陰線",
            'code'  : 'large',
            'trend' : 'shadow'
        },
        'small_shadow' : {
            'name'  : "小陰線",
            'code'  : 'small',
            'trend' : 'shadow'
        },
        'upper_shadow_shadow' : {
            'name'  : "上影陰線",
            'code'  : 'upper_shadow',
            'trend' : 'shadow'
        },
        'lower_shadow_shadow' : {
            'name'  : "下影陰線",
            'code'  : 'lower_shadow',
            'trend' : 'shadow'
        },
        'whisker_shadow' : {
            'name'  : "ヒゲ陰線",
            'code'  : 'whisker',
            'trend' : 'shadow'
        },
        'tower' : {
            'name'  : "塔場",
            'code'  : 'tower',
            'trend' : 'edge'
        },
        'upper_shadow_cross' : {
            'name'  : "うわひげ十字",
            'code'  : 'upper_shadow',
            'trend' : 'edge'
        },
        'cross' : {
            'name'  : "十字",
            'code'  : 'cross',
            'trend' : 'edge'
        },
        'dragonfly' : {
            'name'  : "トンボ",
            'code'  : 'dragonfly',
            'trend' : 'sun'
        },
        'lower_shadow_cross' : {
            'name'  : "しもひげ十字",
            'code'  : 'lower_cross',
            'trend' : 'shadow'
        },
        'four_value_same' : {
            'name'  : "四値同事",
            'code'  : 'four_value_same',
            'trend' : 'edge'
        },
    }
]