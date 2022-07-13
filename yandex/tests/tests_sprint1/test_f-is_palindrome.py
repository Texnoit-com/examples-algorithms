from sprint1.f_is_palindrome import is_palindrome


def test_on_range():
    assert is_palindrome('A man, a plan, a canal: Panama') is True
    assert is_palindrome('zo') is False
    assert is_palindrome('pkgbmg') is False
    assert is_palindrome('e.') is True
    assert is_palindrome('lel') is True
