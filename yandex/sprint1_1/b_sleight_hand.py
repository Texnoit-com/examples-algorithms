'''Тренажёр для скоростной печати

Проверка решения
ID = 69268391'''


from collections import Counter
from typing import List, Tuple

SIZE_FIELD = 4


def sleight_hand(line: str, k: int) -> int:
    '''Подсчет очков в игре Ловкость рук.'''
    amount = Counter(line)
    score: int = 0
    for value in amount.values():
        if value <= 2*k:
            score += 1
    return score


def read_input(size_field: int = SIZE_FIELD) -> Tuple[List[str], int]:
    '''Реализация ввода данных'''
    k: int = int(input())
    line: list = []
    for i in range(size_field):
        line.append(input().replace('.', ''))
    sleight: str = ''.join(line)
    return sleight, k


if __name__ == '__main__':
    line, k = read_input()
    print(sleight_hand(line, k))
