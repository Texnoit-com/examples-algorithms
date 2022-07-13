from sprint1.b_check_parity import check_parity


def test_on_range():
    assert check_parity(a=1, b=2, c=-3) is False
    assert check_parity(a=7, b=11, c=7) is True
    assert check_parity(a=488974850, b=488974850, c=-488974850) is True
    assert check_parity(a=0, b=0, c=0) is True
    assert check_parity(a=0, b=1, c=0) is False
