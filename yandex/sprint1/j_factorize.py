'''Разложение числа на простые множители называется факторизацией числа.
Напишите программу, которая производит факторизацию переданного числа.'''


import math
from typing import List


def factorize(number: int) -> List[int]:
    arr: list = []
    for i in range(2, int(math.sqrt(number))+1):
        while number % i == 0:
            arr.append(i)
            number //= i
    if number != 1:
        arr.append(number)
    return arr


if __name__ == '__main__':
    result = factorize(int(input()))
    print(" ".join(map(str, result)))
