'''Есть упорядоченный массив целых чисел , нужно определить, есть ли в нём число X.'''


def binary_search(array, x):
    left: int = 0
    right: int = len(array)
    while left < right:
        midian = (left + right) // 2
        if array[midian] == x:
            return True
        elif array[midian] < x:
            left = midian + 1
        else:
            right = midian
    return False


if __name__ == '__main__':
    array: int = [5, 7, 9, 12, 15, 18, 19, 20, 22]
    x: int = 20
    print(binary_search(array, x))
