'''Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.

Проверка решения
ID = 69268374'''


from typing import List


def neighboring_zero(home: List[int]) -> List[int]:
    '''Запись расстояние до ближайшего нуля в массиве'''
    zero_left: int = home.index(0)
    for index, element in enumerate(home):
        if element == 0:
            zero_left = index
        else:
            home[index] = abs(index-zero_left)
    home = home[::-1]
    zero_left: int = home.index(0)
    for index, element in enumerate(home):
        if element == 0:
            zero_left = index
        else:
            home[index] = min(abs(index-zero_left), element)
    home = home[::-1]
    return home


def read_input() -> List[int]:
    '''Реализация ввода данных'''
    input()
    home = list(map(int, input().strip().split()))
    return home


if __name__ == '__main__':
    home = read_input()
    print(" ".join(map(str, neighboring_zero(home))))
