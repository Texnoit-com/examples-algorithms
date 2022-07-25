'''Функция должна напечатать все возможные скобочные последовательности
заданной длины в алфавитном (лексикографическом) порядке.'''


def parentheses_generator(length: int,
                          s: str = '',
                          left: int = 0,
                          right: int = 0):
    if left == length and right == length:
        print(s)
    else:
        if left < length:
            parentheses_generator(length, s+'(', left+1, right)
        if right < left:
            parentheses_generator(length, s+')', left, right+1)


if __name__ == '__main__':
    parentheses_generator(2)
