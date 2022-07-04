from sprint1.i_is_power_of_four import is_power_of_four


def test_on_range():
    assert is_power_of_four([-1, -10, -8, 0, 2, 0, 5]) == 3
