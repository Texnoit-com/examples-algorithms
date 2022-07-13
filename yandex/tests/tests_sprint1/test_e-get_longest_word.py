from sprint1.e_get_longest_word import get_longest_word


def test_on_range():
    assert get_longest_word('i love segment tree') == 'segment'
    assert get_longest_word('frog jumps from river') == 'jumps'
    assert get_longest_word(' mymbg') == 'mymbg'
    assert get_longest_word(' wt ') == 'wt'
    assert get_longest_word('eeweee') == 'eeweee'
