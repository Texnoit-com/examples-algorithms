'''Пирамидальная сортировка'''


def heapify(arr, n, i):
    '''Вспомогательная функция'''
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Сравнение левого элемента с корнем
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Сравнение правого элемента с корнем
    if right < n and arr[largest] < arr[right]:
        largest = right

    # сдвинуть корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Вызвать функцию с новым корнем
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print(arr)
