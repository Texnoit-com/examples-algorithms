from sprint2.a_–ľonitoring import –ľonitoring


def test_on_range():
    assert –ľonitoring([['1', '2', '3'],
                       ['0', '2', '6'],
                       ['7', '4', '1'],
                       ['2', '7', '0']]) == [['1', '0', '7', '2'],
                                             ['2', '2', '4', '7'],
                                             ['3', '6', '1', '0']]
