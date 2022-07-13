'''Поиск числа Фибоначчи - динамическое программирование
(запоминания вычислений).'''


def fib(n, lookup):
    '''Вычисляет число и записывает в таблицу,
    при повторной подзадачи, берет готовый вариант'''

    if n <= 1:
        lookup[n] = n
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    return lookup[n]


if __name__ == "__main__":
    n = 34
    lookup = [None] * 101
    print(fib(n, lookup))
