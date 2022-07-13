from sprint1_1.a_neighboring_zero import neighboring_zero


def test_on_range():
    assert(neighboring_zero([0, 1, 4, 9, 0])) == [0, 1, 2, 1, 0]
    assert(neighboring_zero([0, 7, 9, 4, 8, 20])) == [0, 1, 2, 3, 4, 5]
    assert(neighboring_zero([5, 8, 9, 12, 15, 26, 30, 0, 0, 55, 0, 0, 67, 0, 76, 80, 82, 0, 0, 98])) == [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 1, 0, 0, 1]


