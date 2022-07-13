'''Транспонирование матрицы'''


from typing import List


def мonitoring(matrix: List[List[str]]) -> List[List[str]]:
    '''Транспонирование матрицы'''
    if matrix == []:
        return []
    matrix_2: List[List[str]] = []
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix
    if len(matrix[0]) == 1:
        for x in matrix:
            matrix_2.append(x[0])
        return [matrix_2]
    if len(matrix) == 1:
        for y in matrix[0]:
            matrix_2.append([y])
        return matrix_2
    for x in range(len(matrix[0])):
        matrix_3 = []
        for y in range(len(matrix)):
            matrix_3.append(matrix[y][x])
        matrix_2.append(matrix_3)
    return matrix_2


def read_input() -> List[List[str]]:
    n: int = int(input())
    m: int = int(input())
    if n == 0 or m == 0:
        return []
    matrix = []
    for i in range(n):
        matrix.append(input().split(' '))
    return matrix


def print_result(result: List[List[str]]) -> None:
    if result == []:
        print()
    for line in result:
        print(' '.join(line))


if __name__ == '__main__':
    print_result(мonitoring(read_input()))
