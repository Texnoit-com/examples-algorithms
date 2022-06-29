'''Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа. Если все три числа оказываются
одной чётности, игрок выигрывает.Напишите программу, которая по трём числам
определяет, выиграл игрок или нет.'''


def check_parity(a: int, b: int, c: int) -> bool:
    return a % 2 == b % 2 == c % 2


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
