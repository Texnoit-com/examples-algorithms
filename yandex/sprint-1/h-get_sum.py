'''Сумма двоичных чисел без использование встроенного метода'''


from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number = list(map(int, reversed(first_number)))
    second_number = list(map(int, reversed(second_number)))
    size = max(len(first_number), len(second_number))
    first_number += [0]*(size-len(first_number))
    second_number += [0]*(size-len(second_number))
    overflow: int = 0
    res: list = []
    for element in zip(first_number, second_number):
        value = element[0]+element[1]+overflow
        overflow = value//2
        res.append(value%2)
    if overflow == 1:
        res.append(1)
    return ''.join(map (str, reversed(res)))

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
