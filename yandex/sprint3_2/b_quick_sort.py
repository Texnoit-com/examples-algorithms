'''Проверка решения ID = 69574723'''


def partition(members: list, left: int, right: int) -> int:
    '''Перестановка элементов согласно приоритету
    Изменяет глобальный список участников и возвращает опорный эелемент'''
    pivot = members[left]
    border_l = left + 1
    border_r = right - 1
    while True:
        if border_l <= border_r and members[border_r] > pivot:
            border_r -= 1
        elif border_l <= border_r and members[border_l] < pivot:
            border_l += 1
        elif members[border_r] > pivot or members[border_l] < pivot:
            continue

        if border_l <= border_r:
            members[border_l], members[border_r] = members[border_r], members[border_l]
        else:
            members[left], members[border_r] = members[border_r], members[left]
            return border_r


def quick_sort(members: list, left: int, right: int) -> list:
    '''Сортировка элементов'''
    if right - left > 1:
        p = partition(members, left, right)
        quick_sort(members, left, p)
        quick_sort(members, p + 1, right)


def formating(members: list) -> list:
    '''Сохранение элементов с форматированием'''
    return [- int(members[1]), int(members[2]), members[0]]


if __name__ == '__main__':
    number = int(input())
    members = list(formating(input().split()) for _ in range(number))
    left = 0
    quick_sort(members, left, len(members))
    print(*(list(zip(*members))[2]), sep="\n")
