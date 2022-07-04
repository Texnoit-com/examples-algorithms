'''Сортировка слиянием'''


def merge_sort(arr: list) -> None:
    if len(arr) > 1:
        # Нахождение середины массива
        mid = len(arr)//2
        # Разделение массива
        L = arr[:mid]
        R = arr[mid:]
        # Вызов метода для левой части
        merge_sort(L)
        # Вызов метода для правой части
        merge_sort(R)

        i = j = k = 0

        # Копирование элементов во временный массив
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Проверка заполняемости
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    print(arr)
