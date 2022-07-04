from typing import List

from sprint1.c_get_neighbours import get_neighbours


def test_on_range():
    assert get_neighbours(matrix=[[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]], row=3, col=0) == [7, 7]
    assert get_neighbours(matrix=[[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]], row=0, col=0) == [0, 2]
    assert get_neighbours(matrix=[[1], [9]], row=0, col=0) == [9]


def test_on_generate():
    matrix: List[List[int]] = []
    for i in range(11):
        line: List[int] = []
        for j in range(11):
            line.append(i*j)
        matrix.append(line)
    assert get_neighbours(matrix=matrix, row=10, col=10) == [90, 90]
    assert get_neighbours(matrix=matrix, row=9, col=9) == [72, 72, 90, 90]
