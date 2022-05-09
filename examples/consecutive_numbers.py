'''Максимальная длина последовательных единиц в двоичной строке.'''


def max_consecutive(input: str) -> int:
    return max(map(len, input.split('0')))


if __name__ == "__main__":
    input: str = '11000111101010111'
    print(max_consecutive(input))
