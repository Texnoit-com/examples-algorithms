from sprint1.g_to_binary import to_binary


def test_on_range():
    assert to_binary([-1, -10, -8, 0, 2, 0, 5]) == 3
