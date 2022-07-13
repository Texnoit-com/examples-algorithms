from sprint1.g_to_binary import to_binary


def test_on_range():
    assert to_binary(5) == '101'
    assert to_binary(14) == '1110'
    assert to_binary(83) == '1010011'
    assert to_binary(10000) == '10011100010000'
    assert to_binary(2252) == '100011001100'
