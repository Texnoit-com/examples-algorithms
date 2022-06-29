''' Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена 
перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. 
Нужно найти добавленную букву.'''


from collections import Counter
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = Counter(shorter)
    longer = Counter(longer)
    result = longer - shorter
    return ''.join(result.keys())

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
