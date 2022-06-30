'''Для каждого из участков выведите расстояние до ближайшего нуля. 
Числа выводите в одну строку, разделяя их пробелами.

Проверка решения
ID = 69247951'''


from typing import List


def neighboring_zero(home: List[int]) -> List[int]:
    length = len(home)
    zero_left: int = home.index(0)
    for index in range(length):
        if home[index] == 0:
            zero_left = index
        else:
            home[index] = abs(index-zero_left)
    home = home[::-1]
    zero_left: int = home.index(0)
    for index in range(length):
        if home[index] == 0:
            zero_left = index
        else:
            if abs(index-zero_left) < home[index]:
                home[index] = abs(index-zero_left)
    home = home[::-1]
    return home


def read_input() -> List[int]:
    n = int(input())
    home = list(map(int, input().strip().split()))
    return home

home = read_input()
print(" ".join(map(str, neighboring_zero(home))))
