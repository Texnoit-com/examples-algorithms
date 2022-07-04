from sprint1.f_is_palindrome import is_palindrome


def test_on_range():
    assert is_palindrome([-1, -10, -8, 0, 2, 0, 5]) == 3
