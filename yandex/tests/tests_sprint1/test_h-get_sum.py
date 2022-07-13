from sprint1.h_get_sum import get_sum


def test_on_range():
    assert get_sum('1010', '1011') == '10101'
    assert get_sum('1', '1') == '10'
    assert get_sum('10', '0') == '10'
    assert get_sum('0', '0') == '0'
    assert get_sum('0', '10') == '10'
