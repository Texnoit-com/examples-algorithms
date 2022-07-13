'''Поиск числа Фибоначчи - динамическое программирование
(запоминания вычислений). '''


def fib(n):

    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


if __name__ == "__main__":
    n = 34
    print(fib(n))