'''Переводит целое число из десятичной системы в двоичную'''


def to_binary(number: int) -> str:
    b: str = ''
    while number > 0:
        b = str(number % 2) + b
        number = number // 2
    return b


def read_input() -> int:
    return int(input().strip())


if __name__ == '__main__':
    print(to_binary(read_input()))
