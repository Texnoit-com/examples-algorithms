from sprint1.a_evaluate_function import evaluate_function


def test_on_range():
    assert evaluate_function(a=0, x=5, b=8, c=0) == 40
    assert evaluate_function(a=0, x=5, b=0, c=0) == 0
    assert evaluate_function(a=1, x=1, b=1, c=1) == 3
    assert evaluate_function(a=8, x=2, b=9, c=-10) == 40
    assert evaluate_function(a=-8, x=-5, b=-2, c=7) == -183
    assert evaluate_function(a=9, x=-6, b=-4, c=0) == 348
    assert evaluate_function(a=-109, x=-968, b=265, c=-933) == -102393069
