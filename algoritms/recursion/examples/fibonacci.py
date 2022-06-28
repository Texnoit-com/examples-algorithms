'''Задача: написать функцию, которая принимает целое число n и
возвращает n-ное число Фибоначчи.'''


def fibonacci(n):
    SENTINEL = -1
    numbers = [SENTINEL] * (n + 1)

    def fibonacci(n):
        if n <= 1:
            return n
        elif numbers[n] != SENTINEL:
            return numbers[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            numbers[n] = result
            return result
    return fibonacci(n)


if __name__ == '__main__':
    print(fibonacci(10))
