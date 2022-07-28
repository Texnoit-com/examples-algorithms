'''Нужно понять, является ли первая из них подпоследовательностью второй.'''


def subsequence(param1, param2):
    position = -1
    for i in param1:
        position = param2.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    print(subsequence(input(), input()))
