'''Тренажёр для скоростной печати

Проверка решения
ID = 69249752'''


from collections import Counter
from typing import List, Tuple


def sleight_hand(line: List[str], k: int) -> int:
    amount = Counter()
    score: int = 0
    for i in range(len(line)):
        line[i]=line[i].replace('.', '')
        amount += Counter(line[i])
    for value in amount.values():
        if value <= 2*k:
            score += 1
    return score

def read_input() -> Tuple[List[str], int]:
    k: int = int(input())
    line: list = []
    for i in range(4):
        line.append(input())
    return line, k

#line, k = read_input()
#print(sleight_hand(line, k))

assert(sleight_hand(['1231','2..2', '2..2', '2..2'], 3)) == 2
assert(sleight_hand(['1111','9999', '1111', '9911'], 4)) == 1
assert(sleight_hand(['1111','1111', '1111', '1111'], 4)) == 0
assert(sleight_hand(['....','....', '....', '....'], 4)) == 0
