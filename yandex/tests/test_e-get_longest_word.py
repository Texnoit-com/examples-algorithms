from sprint1.e_get_longest_word import get_longest_word


def test_on_range():
    assert get_longest_word([-1, -10, -8, 0, 2, 0, 5]) == 3
