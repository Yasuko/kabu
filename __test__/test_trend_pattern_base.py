import pytest
from trend_pattern_base import (
    detect_bullish_engulfing,
    detect_bearish_engulfing,
    detect_bullish_harami,
    detect_bearish_harami,
    is_dark_cloud_cover,
    detect_piercing_pattern,
    detect_harami_pattern,
    detect_in_neck_pattern,
    detect_on_neck_pattern,
    detect_meeting_lines_pattern,
    detect_bearish_meeting_lines_pattern,
    detect_separating_lines_pattern,
    detect_bearish_separating_lines_pattern,
    detect_tasukigap_pattern,
    detect_bearish_tasukigap_pattern,
    detect_tweezer_top_pattern,
    detect_tweezer_bottom_pattern
)

def test_detect_bullish_engulfing():
    assert detect_bullish_engulfing(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 105, 'high': 110, 'low': 80}
    )
    assert not detect_bullish_engulfing(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_bearish_engulfing():
    assert detect_bearish_engulfing(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 85, 'high': 110, 'low': 80}
    )
    assert not detect_bearish_engulfing(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 95, 'close': 85, 'high': 100, 'low': 80}
    )

def test_detect_bullish_harami():
    assert detect_bullish_harami(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 95, 'close': 98, 'high': 100, 'low': 90}
    )
    assert not detect_bullish_harami(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 95, 'close': 85, 'high': 100, 'low': 80}
    )

def test_detect_bearish_harami():
    assert detect_bearish_harami(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 95, 'close': 92, 'high': 100, 'low': 90}
    )
    assert not detect_bearish_harami(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 95, 'close': 105, 'high': 110, 'low': 90}
    )

def test_is_dark_cloud_cover():
    assert is_dark_cloud_cover(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 95, 'high': 110, 'low': 90}
    )
    assert not is_dark_cloud_cover(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 85, 'high': 110, 'low': 80}
    )

def test_detect_piercing_pattern():
    assert detect_piercing_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 105, 'high': 110, 'low': 80}
    )
    assert not detect_piercing_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_harami_pattern():
    assert detect_harami_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )
    assert not detect_harami_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 105, 'high': 110, 'low': 80}
    )

def test_detect_in_neck_pattern():
    assert detect_in_neck_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 90, 'high': 100, 'low': 80}
    )
    assert not detect_in_neck_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_on_neck_pattern():
    assert detect_on_neck_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 90, 'high': 100, 'low': 80}
    )
    assert not detect_on_neck_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_meeting_lines_pattern():
    assert detect_meeting_lines_pattern(
        {'open': 90, 'close': 110, 'high': 110, 'low': 90},
        {'open': 150, 'close': 110, 'high': 150, 'low': 110}
    )
    assert not detect_meeting_lines_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 100, 'close': 110, 'high': 100, 'low': 80}
    )

def test_detect_bearish_meeting_lines_pattern():
    assert detect_bearish_meeting_lines_pattern(
        {'open': 110, 'close': 90, 'high': 110, 'low': 90},
        {'open': 90, 'close': 110, 'high': 110, 'low': 90}
    )
    assert not detect_bearish_meeting_lines_pattern(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 95, 'high': 110, 'low': 90}
    )

def test_detect_separating_lines_pattern():
    assert detect_separating_lines_pattern(
        {'open': 110, 'close': 85, 'high': 110, 'low': 85},
        {'open': 110, 'close': 150, 'high': 150, 'low': 110}
    )
    assert not detect_separating_lines_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_bearish_separating_lines_pattern():
    assert detect_bearish_separating_lines_pattern(
        {'open': 90, 'close': 110, 'high': 110, 'low': 90},
        {'open': 90, 'close': 50, 'high': 90, 'low': 50}
    )
    assert not detect_bearish_separating_lines_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_tasukigap_pattern():
    assert detect_tasukigap_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 105, 'high': 110, 'low': 80}
    )
    assert not detect_tasukigap_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_bearish_tasukigap_pattern():
    assert detect_bearish_tasukigap_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 89, 'close': 80, 'high': 100, 'low': 75}
    )
    assert not detect_bearish_tasukigap_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

def test_detect_tweezer_top_pattern():
    assert detect_tweezer_top_pattern(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 95, 'high': 110, 'low': 90}
    )
    assert not detect_tweezer_top_pattern(
        {'open': 90, 'close': 100, 'high': 110, 'low': 85},
        {'open': 105, 'close': 85, 'high': 100, 'low': 80}
    )

def test_detect_tweezer_bottom_pattern():
    assert detect_tweezer_bottom_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 105, 'high': 110, 'low': 85}
    )
    assert not detect_tweezer_bottom_pattern(
        {'open': 100, 'close': 90, 'high': 110, 'low': 85},
        {'open': 85, 'close': 95, 'high': 100, 'low': 80}
    )

if __name__ == '__main__':
    pytest.main()