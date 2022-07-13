from sprint1.i_is_power_of_four import is_power_of_four


def test_on_range():
    assert is_power_of_four(15) is False
    assert is_power_of_four(16) is True
    assert is_power_of_four(1) is True
    assert is_power_of_four(4) is True
    assert is_power_of_four(52) is False
