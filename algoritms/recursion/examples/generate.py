'''Дано число N, нужно сгенерировать все правильные 
скобочные последовательности из N открывающих и N закрывающих скобок'''


def generate(n):
    result = []

    def generate_(left, right, accum):
        if not left and not right:
            result.append(''.join(accum))
            return
        if left:
            accum.append('(')
            generate_(left - 1, right, accum)
            accum.pop()
        if right > left:
            accum.append(')')
            generate_(left, right - 1, accum)
            accum.pop()

    generate_(n, n, [])
    return result


if __name__ == '__main__':
    print(generate(3))
