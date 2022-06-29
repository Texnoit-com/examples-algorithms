'''Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано 
количество очков. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, 
сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования 
для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.'''


from typing import List, Optional, Tuple


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set()

    for A in arr:
        Y = target_sum - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)
    return None

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
