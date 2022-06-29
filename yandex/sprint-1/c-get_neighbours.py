'''Дана матрица. Нужно написать функцию, которая для элемента возвращает
всех его соседей. Соседним считается элемент, находящийся от текущего
на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними н
е считаются. Например, в матрице A соседними элементами для (0, 0) будут 2 и 0.
А для (2, 1) –— 1, 2, 7, 7.'''

from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbors = []
    if row-1 >= 0:
        neighbors.append(matrix[row-1][col])
    if row+1 < len(matrix):
        neighbors.append(matrix[row+1][col])
    if col-1 >= 0:
        neighbors.append(matrix[row][col-1])
    if col+1 < len(matrix[0]):
        neighbors.append(matrix[row][col+1])
    neighbors.sort()
    return neighbors


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
