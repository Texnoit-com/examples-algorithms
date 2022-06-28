'''Дан упорядоченный массив и число X, нужно найти максимальный элемент массива, не превосходящего X.
Если такого элемента не существует, вернуть -1.'''


def max_to_border(array, x):
    if not array or array[0] > x:
        return -1

    left: int = 0
    right: int = len(array)
    while left + 1 < right:
        midian = (left + right) // 2
        if array[midian] <= x:
            left = midian
        else:
            right = midian
    return array[left]


if __name__ == '__main__':
    array: int = [5, 7, 9, 12, 15, 18, 19, 20, 22]
    x: int = 17
    print(max_to_border(array, x))
