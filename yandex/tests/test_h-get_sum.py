from sprint1.h_get_sum import get_sum


def test_on_range():
    assert get_sum([-1, -10, -8, 0, 2, 0, 5]) == 3
