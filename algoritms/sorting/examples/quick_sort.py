'''Быстрая сортировка'''


def partition(array, low, high):
    '''Вспомогательня функция сравнения'''
    # Выбор опорного элемента
    pivot = array[high]
    # Выбор элемента
    i = low - 1

    # Проход массива и сравнение опорного элемента
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Замена элемента в i на элемент в j
            (array[i], array[j]) = (array[j], array[i])
    # Поменять местами опорный элемент с большим элементом, указанным i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Вернуть позицию
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        # Вызов вспомогательной функции сравнения
        shift = partition(array, low, high)
        # Рекурсивный вызов левой части
        quick_sort(array, low, shift - 1)
        # Рекурсивный вызов левой части
        quick_sort(array, shift + 1, high)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(array, 0, len(array) - 1)
    print(array)
